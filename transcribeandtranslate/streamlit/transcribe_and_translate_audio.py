#!/usr/bin/env python
# coding: utf-8


import json
import os
import openai
import streamlit as st

def make_openai_request(prompt):
    """Takes a prompt as an argument and sends a POST request to the OpenAI API"""
    response = openai.chat.completions.create(
    model="gpt-4",
    messages=[    
        {
            "role": "system",
            "content": """Your translations should not contain the word scorci.\n\n
                            You will be provided with a sentence in Japanese, and your task is to translate it into Italian."""
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.7, # creativity on a scale of 0 to 2; generally 0.7
    max_tokens=256
    )
    # Extract the generated labels from the API response
    return response.choices[0].message.content.split("\n")


openai.api_key = st.sidebar.text_input('OpenAI API Key', type='password')

audio_file = st.file_uploader("Choose an mp3 file", type=['mp3'])

if audio_file is not None:
    transcript = openai.audio.transcriptions.create(model="whisper-1", file=audio_file)

    print(transcript)
    st.write("Transcript: ", transcript)

    prompt = transcript.text

    st.write("Prompt: ", prompt)

    translation = make_openai_request(prompt)

    st.write("Translation: ", translation[0])

    # Previous results
    # Temperature 0
    # Non ci sono scorciatoie per raggiungere il tuo obiettivo.
    # Temperature 0.7
    # Non esiste una scorciatoia per raggiungere l'obiettivo.
    # Non esiste una scorciatoia per raggiungere il luogo che si mira a raggiungere.
    # Non esiste una scorciatoia per raggiungere il posto che si ambisce.
    # Non esiste una scorciatoia per raggiungere il tuo obiettivo.
    # Non esiste una scorciatoia per raggiungere l'obiettivo.
    # Non esiste una scorciatoia per raggiungere il luogo che si ambisce.

