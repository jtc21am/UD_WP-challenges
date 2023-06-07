'''Read the NBA finals CSV data into one more more data structures as needed to complete the following:
[ ] Print out a ranking of who has won the MVP more than once, by times won, e.g. this output:
    - 6 times: Michael Jordan
    - 3 times: Shaquille O'Neal, LeBron James
    - 2 times: <etc>'''
'Luke/Saul'
#Year,Winner,Loser,Score,MVP
#0    ,1    , 2   , 3    , 4
# import CSV, import collections
# create function
# create a variable to stores the collections counter
# open the csv file, then use a For Loop to iterate through the rows of the csv file
# Use an if statement to check if MVP is blank:
# if not, add the MVP to the counter, and add 1
# return MVP collection

# create a 2nd function to sort the MVP
# convert the collection to a dictionary, use the sort function to sort by highest count, (reverse)
# find most wins

# create a 3rd function to print the output as prescribed 
# winners = empty list
# loop through the dictionary
#  if player wins = most wins 
#   add the player name to the list
# if player wins < most wins:
#   create a string of the winners list using Join
#   print statement using most wins times: then joined string
#   then save new player's win value as most wins
#   clear winner list by over writing it with new players name

import csv
import collections
import operator

def count_mvp():
    mvp = collections.Counter()
    with open('nba_finals.csv', newline='') as nbafinals:
        nbafinals = csv.DictReader(nbafinals)
        for row in nbafinals:
            if row.get("MVP") != "":
                mvp[row.get("MVP")] += 1
        return flip_mvp(dict(mvp))

def flip_mvp(mvp):
    flipped_mvp = {}
    for key, value in mvp.items():
        if value in flipped_mvp:
            flipped_mvp[value].append(key)
        else:
            flipped_mvp[value] = [key]
    return print_by_wins(flipped_mvp)
    

def print_by_wins(flipped_mvp):
    for key, value in (dict(sorted(flipped_mvp.items(), key=operator.itemgetter(1),reverse=True))).items():
        if key >= 2:
            print(f'{key} times: {", ".join(value)}')

(count_mvp())