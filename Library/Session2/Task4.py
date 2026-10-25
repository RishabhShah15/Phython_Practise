#Suppose you have a NumPy array of product prices from Flipkart. Use broadcasting to apply a 10% discount to all prices and print the new array.<br><br><em><strong>Constraint:</strong> Do not use any loops.</em>

import numpy as np


prices = np.array([499, 1299, 2499, 799, 15499])

discounted_prices = prices * 10/100

print("Original Prices:   ", prices)
print("Discounted Prices: ", discounted_prices)

final_price=prices-discounted_prices
print ("final price:",final_price)