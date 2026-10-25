#Use np.arange() to generate an array of order IDs for 10 consecutive Zomato orders starting from 101. Print the array and its size.

import numpy as np

# Generate 10 consecutive order IDs starting from 101
order_ids = np.arange(101, 111)

# Print the array and its size
print("Order IDs:", order_ids)
print("Size:", order_ids.size)