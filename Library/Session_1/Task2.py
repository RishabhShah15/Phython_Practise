#Create a NumPy array called followers using np.array() that stores the follower counts for 5 Instagram influencers: [1200, 15000, 67000, 340000, 1250000]. Print the array, its shape, number of dimensions, and data type.

import numpy as np

followers = np.array([1200, 15000, 67000, 340000, 1250000])

print("Followers Array:", followers)
print("Shape:", followers.shape)
print("Number of dimensions:", followers.ndim)
print("Data type:", followers.dtype)