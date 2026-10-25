#Create a NumPy array of IPL team scores for 8 matches. Use fancy indexing to select the scores from matches 2, 5, and 7, and print them.

import numpy as np

scores = np.array([178, 205, 164, 192, 218, 145, 189, 210])

selected_indices = [2, 5, 7]
selected_scores = scores[selected_indices]

print("All Scores:", scores)
print("Scores for Matches 2, 5, and 7:", selected_scores)
