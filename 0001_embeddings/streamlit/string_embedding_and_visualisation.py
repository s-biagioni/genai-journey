#!/usr/bin/env python
# coding: utf-8

import os
import openai
import seaborn
from scipy import spatial
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import streamlit as st


st.title("Create Embeddings and Visualise 2D PCA")

st.info("""Please enter your OpenAI key in the panel on the left 
            and write the 3 strings to create and visualise their embeddings.""")

# The OpenAI key is stored in a file.
openai.api_key = st.sidebar.text_input('OpenAI API Key', type='password')


string1 = st.text_input(
    "Enter some text 👇",
    placeholder="string 1",
)

string2 = st.text_input(
    "Enter some text 👇",
    placeholder="string 2",
)

string3 = st.text_input(
    "Enter some text 👇",
    placeholder="string 3",
)

if string1 and string2 and string3 and openai.api_key.startswith('sk-'):
    # https://platform.openai.com/docs/guides/embeddings/what-are-embeddings?lang=python

    response = openai.embeddings.create(
        input=[string1, string2, string3],
        model="text-embedding-3-small"
    )

    # print(response)
    # print(response.data[0].embedding)
    # print(response.data[1].embedding)
    # print(response.data[2].embedding)


    # https://stackoverflow.com/a/18424933

    cosine_similarity1 = 1 - spatial.distance.cosine(response.data[0].embedding, response.data[1].embedding)

    st.write('cosine similarity(string1, string2): ')
    st.write(cosine_similarity1)

    cosine_similarity2 = 1 - spatial.distance.cosine(response.data[1].embedding, response.data[2].embedding)

    st.write('cosine similarity(string2, string3): ')
    st.write(cosine_similarity2)

    cosine_similarity3 = 1 - spatial.distance.cosine(response.data[0].embedding, response.data[2].embedding)

    st.write('cosine similarity(string1, string3): ')
    st.write(cosine_similarity3)

    # heatmap among equal strings
    seaborn.heatmap([response.data[0].embedding[:20], response.data[1].embedding[:20],response.data[2].embedding[:20]], 
                    cbar=False, xticklabels=False, yticklabels=[string1, string2, string3]
                    )

    # https://discuss.streamlit.io/t/how-to-display-matplotlib-graphs-in-streamlit-application/35383/2
    st.pyplot(plt.gcf()) # instead of plt.show()

    # store the embeddings in a 2d numpy array
    embeddings = [response.data[0].embedding, 
                response.data[1].embedding, 
                response.data[2].embedding]
    embeddings_array = np.array(embeddings)

    st.write("Shape: " + str(embeddings_array.shape))
    st.write(embeddings_array)


    # reducing the embedding dimension with PCA
    # https://learn.deeplearning.ai/courses/google-cloud-vertex-ai/lesson/4/visualizing-embeddings

    # Perform PCA for 2D visualization
    PCA_model = PCA(n_components = 2)
    PCA_model.fit(embeddings_array)
    new_values = PCA_model.transform(embeddings_array)


    st.write("PCA Shape: " + str(new_values.shape))
    st.write(new_values)


    st.write(new_values[:,0])
    st.write(new_values[:,1])


    colours = ListedColormap(['r','b','g'])
    values = [0, 1, 2]
    scatter = plt.scatter(new_values[:,0], new_values[:,1], c=values, cmap=colours)
    classes = [string1, string2, string3]
    #plt.legend(handles=scatter.legend_elements()[0], labels=classes)

    #plt.axis('square')

    # https://discuss.streamlit.io/t/how-to-display-matplotlib-graphs-in-streamlit-application/35383/2
    st.pyplot(plt.gcf()) # instead of plt.show()

