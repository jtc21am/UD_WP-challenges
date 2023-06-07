'''Billboard Hot 100 of 2000
[ ] What artist had the most songs chart in 2000, and what were those songs?
rank,song,artist,last-week,peak-rank,weeks-on-board,date
Saul
'''
# could there be a tie?
#output would be artist and song
# import csv, and pandas
# use a dataframe to only grab the columns I need, and remove duplicate rows
# use value counts to count the artist occurences
# find the max # of the occurences in case there is a tie
# use an if statement to print the artists and associated songs should the # of songs be the max for that artist

# import csv
# import pandas as pd

# def read_csv(filename):
#     song_dataframe = pd.read_csv(filename, usecols = ['artist', 'song'])
#     no_song_dups = song_dataframe.drop_duplicates(keep='first')
#     songs_per_artist = no_song_dups['artist'].value_counts().to_dict()
#     most_artists = [key for key in songs_per_artist if songs_per_artist[key]==max(songs_per_artist.values())]
#     for x in most_artists:
#          print(no_song_dups.query('artist == @x'))
# read_csv('billboard100_2000.csv')


import csv
import collections

def count_songs(filename):
    songs_no_dups = dict()
    artist_count = collections.Counter()
    with open(filename, newline='') as csv1:
        for row in csv.reader(csv1):
            songs_no_dups[row[1]] = row[2]
    #count frequency of artist
    for artist in songs_no_dups.values():
        artist_count[artist] +=1
    #convert collection counter to dict
    artist_count_dict = dict(artist_count) 
    #find max # of songs   
    artist_count_max = max(artist_count_dict.values())
    #make list of artist names whose total # of songs equals max # songs
    artists_most_songs = [key for key, value in artist_count_dict.items() if value == artist_count_max]
    print(f'Artist(s) with most songs on Billboard 100 in Year 2000 is {artists_most_songs}.  The songs are:')
    #print each song for each artist who has the max song for the billboard year
    for key,value in songs_no_dups.items():
        for artist in artists_most_songs:
            if value == artist:
                print(f'{value} by {key}')
count_songs('billboard100_2000.csv')
