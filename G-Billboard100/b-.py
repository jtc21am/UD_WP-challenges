'''Billboard Hot 100 of 2000
[ ] What song was the #1 song for the most weeks of 2000, who was the artist, and how many weeks was it at #1?
rank,song,artist,last-week,peak-rank,weeks-on-board,date
luke
'''

#output of choice
#edge case - if tie, print all
#find edge case if the total is 52 weeks, and do the for loops
# import csv, import pandas
#create a function which takes in a cvsfile
#read csv, use pandas to save only rank, artist, song
#use panda query to find only rank #1
# value count method to count the # of times the song appear as #1
# use a for loop to check for ties and return the song  - do second after
# call the function passing the csv as arguement

import csv
import pandas as pd

def most_num_one_songs(csvfile):
    songs_df = pd.read_csv(csvfile, usecols=['rank','artist', 'song'])
    songs_num_one_only = songs_df.query('rank == 1')
    
    frequency_num_one = songs_num_one_only[['artist','song']].value_counts().to_frame()
    print(frequency_num_one)
    frequency_num_total = songs_num_one_only['artist'].count().sum()
    #print those rows with that equal max count
    frequency_num_max = frequency_num_one.query('count == count.max()')
    print(frequency_num_total)
    return(frequency_num_max)

print(most_num_one_songs('billboard100_2000.csv'))