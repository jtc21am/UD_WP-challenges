'''This is a CSV that we recommend parsing with a CSV parsing library (versus parsing it yourself).
[ ] What is the distribution of ratings? (How many are PG, PG-13, R, etc.?)                                                                              
Title,Distributor,Release Date,US Sales,World Sales,Runtime,Rating 

Sara
'''
#import csv, import collections
#create a function which takes in the cvsfile as a parameter
#create the collections Counter
#open the csv file and iterate through the rows using Dictionary reader
#for each rating add it to the counter, and add 1 for the frequency
#return the sorted collection by rating count
#call the function, pass the arguement of the file name, print

import csv
import collections

def ratings_counter(csvfile):
    ratings_count = collections.Counter()
    with open(csvfile, newline='') as csvreader:
        for row in csv.DictReader(csvreader):
            ratings_count[row['Rating']] +=1
    sorted_counts = (sorted(ratings_count.items(), key=lambda n: (n[1])))
    print(type(ratings_count[0]))
    print((sorted_counts))

print(ratings_counter('top_movies.csv'))





