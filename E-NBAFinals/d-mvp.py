'''Read the NBA finals CSV data into one more more data structures as needed to complete the following:
[ ] Print out a ranking of who has won the MVP more than once, by times won, e.g. this output:
    - 6 times: Michael Jordan
    - 3 times: Shaquille O'Neal, LeBron James
    - 2 times: <etc>'''
'Luke'
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

def count_mvp():
    mvp = collections.Counter()
    with open('nba_finals.csv', newline='') as nbafinals:
        for row in csv.reader(nbafinals):
            if row[4] != "":
                mvp[row[4]] += 1
        return sort_mvp(mvp)
    # key:Value
    #MJ:6
    #6:MJ
    #3 : [SO, LB]
    

def sort_mvp(mvp):
    sorted_mvp = dict(sorted(mvp.items(), key=lambda pair: pair[1], reverse=True))
    first_pair = next(iter((sorted_mvp.items())))
    highest_mvp_value = first_pair[1]
    return print_by_wins(sorted_mvp, highest_mvp_value)

def print_by_wins(sorted_mvp, highest_mvp_value):
    winners = []
    for element in (sorted_mvp.items()):
        if element[1] == highest_mvp_value:
            winners.append(element[0])
        if element[1] < highest_mvp_value:
            winners_as_comma = ', '.join(winners)
            print(f'{highest_mvp_value} times: {winners_as_comma}')
            winners = [element[0]]
            highest_mvp_value = element[1]

count_mvp()