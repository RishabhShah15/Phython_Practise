#Find a public JSON file of trending movies 
# (or create your own movies.json with at least 3 movie objects containing title, year, and rating),
#  then use the json module in Python to load the file and print the title and rating of each movie.
import json
file=open('C:\\Python\\session_14\movies.json','r')

movies=json.load(file)

for movie in movies:
    print(f" {movie['title']} -- Rating {movie['rating']}")
