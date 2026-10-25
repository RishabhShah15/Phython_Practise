#Use the pathlib module to check if a file called 'my_fav_apps.json' exists in your current directory, 
#and if not, create it and write a JSON array of your top 3 mobile apps (e.g., Instagram, Zomato, Paytm) with their names and categories.
# <br><br><em><strong>Hint:</strong> Use Path('my_fav_apps.json').exists() to check for the file, and json.dump() to write the data.</em>

import pathlib as p
import json

file_path=p.Path('C:\Python\session_14\my_fav_apps.json')

if not file_path.exists():
    fav_apps=[{"name":"Instagram","category":"social Media"},
     {"name": "Zomato", "category": "Food Delivery"},
        {"name": "Paytm", "category": "Finance"}
        ]
    with open(file_path,'w') as file:
        json.dump(fav_apps,file)

        print("my_fav_apps.json was created successfully.")

else:
   with open(file_path,'r') as fiel_read:
        data=json.load(fiel_read)
        print(data)
