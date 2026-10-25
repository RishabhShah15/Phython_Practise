#Given a NumPy array of daily steps tracked for 10 days, use boolean indexing to select only the days where the steps were greater than 8000.<br><br><em><strong>Hint:</strong> Use an array like steps = np.array([7500, 8200, 9000, ...]) and apply a boolean condition.</em>


import numpy as np

daily_steps = np.array([6500, 8200, 9100, 7400, 8050, 11200, 5300, 8900, 7800, 10400])

print(daily_steps)

mask = daily_steps > 8000

print(mask)

more_8000=daily_steps[mask]

print(more_8000)

