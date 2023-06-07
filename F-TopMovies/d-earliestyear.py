'''This is a CSV that we recommend parsing with a CSV parsing library (versus parsing it yourself).
                                                                        
[ ] What is the earliest year on this list, and what were the films from that year?
Title,Distributor,Release Date,US Sales,World Sales,Runtime,Rating
'''
#import csv
#create a function that takes in the file
#create an empty dictionary, key - year, value [movies]
#open the csv and save the output as a new file
#find the earliest year based on the release date
#return the year, and the movies from that year

import csv

def movies_by_year (csvfile):
    year_movie = {}
    with open(csvfile, newline = '') as topmovies:
        movie_list = csv.DictReader(topmovies)
        earliest_year = min(movie_list, key=lambda n: n["Release Date"])
        return earliest_year["Release Date"], earliest_year["Title"]

print(movies_by_year('top_movies.csv'))