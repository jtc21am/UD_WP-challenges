'''This is a CSV that we recommend parsing with a CSV parsing library (versus parsing it yourself).
[ ] What distributor has the most films on this list?  
Title,Distributor,Release Date,US Sales,World Sales,Runtime,Rating
Jessica '''                                                                          

#import csv, import collections
#create funciton which takes in the csvfile name
#create the variable collector
#open the csv file and iterate through it one row at time
#for each  dictributor name, add to the collection and add one to the counter
#return the max of the collections

import csv
import collections

def count_distributors(csvfile) -> str:
    distributors = collections.Counter()
    with open(csvfile, newline ='') as distributor_csv:
        for row in csv.DictReader(distributor_csv):
            distributors[row["Distributor"]] +=1
        print(distributors)
        return max(distributors)

print(count_distributors('top_movies.csv'))