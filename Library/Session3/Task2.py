#Simulate a Spotify-like 'Recommended Songs' feature: Given two 3x3 matrices representing user-song interaction scores (user preferences and song popularity), use dot() and matmul() to compute the final recommendation matrix and explain the difference between the two results.


import numpy as np

user_preferences = np.array([
    [1, 2, 3],
    [3, 2, 1],
    [4, 2, 1]
])


song_characteristics = np.array([
    [3, 2, 1],
    [1, 2, 3],
    [4, 2, 2]
])


matmul = np.matmul(user_preferences, song_characteristics)
print("Matmul :",matmul)
dot = np.dot(user_preferences, song_characteristics)
print("Dot :",dot)
print("identical results", np.array_equal(matmul, dot))