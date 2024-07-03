import streamlit as st
import requests
import base64


st.title("Office Dress Code Adviser")


st.info("""
        Please firstly enter your OpenAI API key in the panel on the left. <br> 
        If you don't have an OpenAI API key, you can get one by following the instructions in the [OpenAI API documentation](https://platform.openai.com/docs/quickstart/account-setup).
""")

openai_api_key = st.text_input('OpenAI API Key', type='password')

# Upload an image using streamlit
uploaded_file = st.file_uploader("Choose an image of your colleagues...", type="jpg")

if uploaded_file and openai_api_key.startswith('sk-'):

    # Getting the base64 string
    base64_image = base64.b64encode(uploaded_file.read()).decode('utf-8')

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

    st.write(response_content)