'''This is a CSV that we recommend parsing with a CSV parsing library (versus parsing it yourself).
[ ] What is the highest grossing movie from Universal Pictures, domestically?
Jessica'''
# Title,Distributor,Release Date,US Sales,World Sales,Runtime,Rating
#import csv
#create a function taking in the csvfile as the parameter -- returning a string
#create an empty dictionary
# open the csv and iterater through them
# use an if statement to check if the distributor is Universal
# if True, add the movie title as the key, and value will be the US Sales
#return max of the dictionary onl the movie title

import csv

def movies(csvfile) -> str:
    universal_movies = {}
    with open(csvfile, newline='') as universalmovies:
        for row in csv.DictReader(universalmovies):
            if row["Distributor"] == "Universal Pictures":
                universal_movies [row["Title"]] = int(row['US Sales'])
        return max(universal_movies.items(), key=lambda n: (n[1]))[0]
    
print(movies('top_movies.csv'))