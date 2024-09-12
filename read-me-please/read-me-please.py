import os
from openai import OpenAI

client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY"),
)

# https://platform.openai.com/docs/guides/chat-completions
completion = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages=[{"role": "user", "content": "what's the meaning of life?"}]
)

# Get the generated answer
answer = completion.choices[0].message.content

# print(answer)

# https://platform.openai.com/docs/guides/text-to-speech
# possible voices: alloy, echo, fable, onyx, nova, and shimmer
with client.audio.speech.with_streaming_response.create(
    model="tts-1",
    voice="alloy",
    input=answer,
) as response:
    response.stream_to_file("speech.mp3")
