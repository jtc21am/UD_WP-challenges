'''Billboard Hot 100 of 2000
[ ] What song(s) were on the charts (anywhere on the charts) for the most weeks of 2000?
Jessica'''
# rank,song,artist,last-week,peak-rank,weeks-on-board,date
# based on question, ensure that ties are taken into account for output

# Use a collection counter to count the song frequency
# find the max of the collection, use values
# use a for loop to print the songs that have the counter value of the max

import csv
import collections

def find_most_charted_songs(filename):
    song_most_charted = collections.Counter()
    with open(filename, newline='') as csvfile:
        for row in csv.DictReader(csvfile):
            song_most_charted[row['song']] += 1
        most_charted_count = max(song_most_charted.values(), key = lambda x:int(x))
        songs_with_most_charted_count = [song for song in song_most_charted if song_most_charted[song] == most_charted_count]
        print(song_most_charted)
        print(songs_with_most_charted_count)

find_most_charted_songs('billboard100_2000.csv')


