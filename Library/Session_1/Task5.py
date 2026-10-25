#Convert a Python list of cricket scores [45, 67, 120, 89, 54] to a NumPy array, then use the .itemsize attribute to print how many bytes each score takes in memory.<br><br><em><strong>Hint:</strong> Use np.array() for conversion and .itemsize for memory size.</em>

import numpy as np

scores =[45, 67, 120, 89, 54]

arry_score=np.array(scores)

print(f"Score array :",arry_score)
print(f"Score array bytes :",arry_score.itemsize)

