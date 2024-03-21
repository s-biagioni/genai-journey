#!/usr/bin/env python
# coding: utf-8

# # Translation Using the Library

# In[484]:


# !pip install openai


# In[485]:


import json
import os
import openai


# In[486]:


key_location = '/Users/silvi/Downloads/key-location/genaikey.txt'

with open(key_location, 'r') as file:
    key = file.readline().strip()


# In[487]:


openai.api_key = key


# In[488]:


audio_file= open(
    "./JapaneseQuote.mp3"
    , "rb")
transcript = openai.audio.transcriptions.create(model="whisper-1", file=audio_file)

print(transcript)


# In[489]:


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


# In[490]:


prompt = transcript.text


# In[491]:


print(prompt)


# In[492]:


translation = make_openai_request(prompt)


# In[493]:


print(translation[0])

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

