import os
import base64
import requests

openai_api_key = os.environ.get('OPENAI_API_KEY')

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "C:\\Users\\silvi\\Downloads\\Tanfield Edinburgh WD 1.jpg"

# Getting the base64 string
base64_image = encode_image(image_path)

if openai_api_key:
    # Use the value of OPENAI_API_KEY
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }

    payload = {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": """
                                    Can you suggest the likely dress code for this office based on the clothing seen in the picture?

                                    Please, also make suggestions on the type of clothing that would be appropriate for this office for a man and a woman.
                                """
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 1000
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    print(response.json())

    response_content = response.json()['choices'][0]['message']['content']
    print(response_content)
else:
    print("OPENAI_API_KEY environment variable is not set.")




