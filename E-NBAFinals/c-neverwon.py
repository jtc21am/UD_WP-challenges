'''Read the NBA finals CSV data into one more more data structures as needed to complete the following:
[ ] Which teams have made it to the NBA finals but have never won?
'''
#output = list
#if no teams satisfy the scenario, empty list is ok

#import csv
#create function
# create 2 sets, one for winners, one for losers
# open the csv file, use reader to save the lines into a new file
# skip the header row of the reader file -- using next
# iterate through the reader file one row at a time
# save winner --> index 1 into set for winners
# same as above from index 2 for losers
# create a list of the difference between the winner set and the loser set
# return the list

# call the function and print the list

import csv

def losers() -> list:
    teams_won = set()
    teams_lost = set()
    with open('nba_finals.csv', newline='') as csvfile:
        nba_reader = csv.reader(csvfile) #O(n)
        next(nba_reader)
        for row in nba_reader: #O(n)
            teams_won.add(row[1])
            teams_lost.add(row[2])
        never_won = list(teams_lost - teams_won)  #O(n)
        # teams_never_won = list(never_won)
        # for team in never_won:
        #     teams_never_won.append(team)
    return never_won

print(losers())



