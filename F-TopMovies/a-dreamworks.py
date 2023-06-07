'''This is a CSV that we recommend parsing with a CSV parsing library (versus parsing it yourself).
[ ] What movies on this list were distributed by DreamWorks?
Ryan Saul'''

#output : a list is ok
# Title,Distributor,Release Date,US Sales,World Sales,Runtime,Rating
# Title - 0, Distributor - 1
#Dreamworks appears as two different versions, consider both

#import csv
#create a function:
#create an empty list to hold the movie names
#open the csv file and not save it
#Use a FOR loop to iterate through the csv file (using the csv reader)
# Use an IF statement to test whether DreamWorks is in the string
# if true, add the Title to the list
#return the movie list

# call the function and print

import csv
def dreamworks_movies() -> list:
    movies = []
    with open('top_movies.csv', newline='') as topmovies:
        for row in csv.reader(topmovies):
            if "DreamWorks" in row[1]:
                movies.append(row[0])
        return movies

print(dreamworks_movies())