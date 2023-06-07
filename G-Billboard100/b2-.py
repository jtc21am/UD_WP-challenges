import csv
import collections

def find_num_one_songs(csvfile):
    with open(csvfile, 'r') as songcsv:
        song_data = csv.reader(songcsv, delimiter=",")
        #find songs that have rank =1
        num_ones_only = filter(lambda x: (x[0] =="1"), song_data)
        # create list of the #1 joining the song and artist using Slicing
        remove_dup_songs = list(map(lambda x:(' - '.join(x[1:3])), num_ones_only))
        #count the frequency of the song on the list and save as dict
        ratings_count = dict(collections.Counter(remove_dup_songs))
        #find and print all songs that have most weeks at #1
        max_song = max(ratings_count.values())
        for key, value in ratings_count.items():
            if value == max_song:
                print(f' The song and artist, {key}, was Number #1 for {value} weeks.')

find_num_one_songs('billboard100_2000.csv')
