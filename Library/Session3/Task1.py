#Create two NumPy arrays representing the daily step counts of two friends over a week and use element-wise addition, subtraction, multiplication, and division to compare their activity levels.

import numpy as np


friend_a = np.array([8500, 10200, 6400, 9100, 11500, 4800, 12000])
friend_b = np.array([7200,  9800, 7500, 8900, 10400, 6200, 11000])


Additions = friend_a + friend_b

print(f"Addition of a and b",Additions)


Substraction = friend_a - friend_b

print(f"Substraction of a and b",Substraction)


Multiplication = friend_a * friend_b

print(f"Multiplication of a and b",Multiplication)

Divisions = friend_a / friend_b

print(f"Divisions of a and b",Divisions)