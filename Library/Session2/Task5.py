#Given a NumPy array of user ratings (can be negative, zero, or positive) for songs on Spotify, use boolean masking to set all negative ratings to zero, keeping other ratings unchanged.


import numpy as np

User_ratings = np.array([3.5, -2.0, 4.0, -1.5, 0.0, -5.0, 2.5])


User_ratings[User_ratings < 0] = 0

print("Ratings:", User_ratings)