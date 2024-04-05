#!/usr/bin/env python
# coding: utf-8



import os
import openai
import seaborn
from scipy import spatial
import numpy as np
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap





# The OpenAI key is stored in a file.
key_location = '/Users/silvi/Downloads/key-location/genaikey.txt'

with open(key_location, 'r') as file:
    key = file.readline().strip()


openai.api_key = key


string1 = "A koala jumped from a tree"
string2 = "A koala is on a tree"
string3 = "I like pizza"


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

print('cosine similarity(string1, string2): ')
print(cosine_similarity1)

cosine_similarity2 = 1 - spatial.distance.cosine(response.data[1].embedding, response.data[2].embedding)

print('cosine similarity(string2, string3): ')
print(cosine_similarity2)

cosine_similarity3 = 1 - spatial.distance.cosine(response.data[0].embedding, response.data[2].embedding)

print('cosine similarity(string1, string3): ')
print(cosine_similarity3)



# heatmap among equal strings
seaborn.heatmap([response.data[0].embedding[:20], response.data[1].embedding[:20],response.data[2].embedding[:20]], 
                cbar=False, xticklabels=False, yticklabels=[string1, string2, string3]
                )

plt.show()

# store the embeddings in a 2d numpy array
embeddings = [response.data[0].embedding, 
              response.data[1].embedding, 
              response.data[2].embedding]
embeddings_array = np.array(embeddings)

print("Shape: " + str(embeddings_array.shape))
print(embeddings_array)



# reducing the embedding dimension with PCA
# https://learn.deeplearning.ai/courses/google-cloud-vertex-ai/lesson/4/visualizing-embeddings

# Perform PCA for 2D visualization
PCA_model = PCA(n_components = 2)
PCA_model.fit(embeddings_array)
new_values = PCA_model.transform(embeddings_array)


print("Shape: " + str(new_values.shape))
print(new_values)


print(new_values[:,0])
print(new_values[:,1])


colours = ListedColormap(['r','b','g'])
values = [0, 1, 2]
scatter = plt.scatter(new_values[:,0], new_values[:,1], c=values, cmap=colours)
classes = [string1, string2, string3]
plt.legend(handles=scatter.legend_elements()[0], labels=classes)

plt.axis('square')

plt.show()

