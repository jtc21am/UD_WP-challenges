'''Billboard Hot 100 of 2000
[ ] Print out all of the #1 songs and the artists who made them. If a song was #1 for more than one week, only print it once. Example output:

    These were the number one songs of 2000:
    "Try Again" - Aaliyah
    "Say My Name" - Destiny's Child
    "What A Girl Wants" - Christina Aguilera
    "Maria Maria" - Santana Featuring The Product G&B
    "Smooth" - Santana Featuring Rob Thomas
    "Independent Women Part I" - Destiny's Child
    
Carol'''
#keep format of the example - song, hyphen, artist
# rank,song,artist,last-week,peak-rank,weeks-on-board,date
#import csv
#use conxtext mgr to open the file and save it

#create a fuction which takes in the csv file as the parameter
#filter the rows by rank, index 0, only if rank =1, and save this data as a new file
# remove the duplicates, and use join to create the expected output with a hyphen, only need song, artist
#create a print statement for the prompt 
#use a for loop to print the songs, one row at a time
#call function

import csv

def find_num_one_songs(csvfile):
    with open(csvfile, 'r') as songcsv:
        song_data = csv.reader(songcsv, delimiter=",")
        num_ones_only = filter(lambda x: (x[0] =="1"), song_data)
        remove_dup_songs = set(map(lambda x:('"' + x[1] + '"' + ' - ' + x[2]), num_ones_only))
        print("These were the number one songs of 2000: ")
        for song in remove_dup_songs:
            print(song)
find_num_one_songs('billboard100_2000.csv')




