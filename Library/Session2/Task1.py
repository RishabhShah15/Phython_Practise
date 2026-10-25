#Create a 2D NumPy array representing the ratings (out of 5) given by 4 users to 5 different food items on Zomato. Use slicing to extract the ratings given by the second and third users only.

import numpy as np


ratings = np.array([
    [5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5],
    [3, 4, 5, 4, 3],
    [5, 3, 4, 5, 4] 
])

selected_ratings = ratings[1:3]

print(ratings)

print("2nd and 3rd users rating:",selected_ratings)