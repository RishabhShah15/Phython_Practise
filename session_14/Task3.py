#Download a sample CSV file of IPL match scores 
# (you can create your own with columns: match_id, team1, team2, winner) 
# and write a Python script to read the file and print the winner of each match using the csv module.

import csv
with open('C:\\Python\session_14\\ipl_match_scores.csv','r')as f:
    for IPL in csv.reader(f):
        print(f'Winner is {IPL[3]}')
