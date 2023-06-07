'''Read the NBA finals CSV data into one more more data structures as needed to complete the following:

[ ] Which teams have made it to the NBA finals but have never won?
Write a function that takes as an argument a year and returns the winner of the NBA finals that year.
Carol'''
# Year,Winner,Loser,Score,MVP

#import csv
#create a function which takes in 1 parameter (year --> integer)
#use list comprehension to open the csv file, and save the contents
#use a FOR loop to iterate through the new file
# if element in index 0 is equal tot he year selected
#   If true return element in index 1 which is the team name

#create a variable which is equal to the year selected
#print and call the function passing in the new variable for the year selected)

import csv

def winning_team(year: str) -> str:
    with open('nba_finals.csv') as csvfile:
        nba_reader = csv.DictReader(csvfile)
        for row in nba_reader:
            if row["Year"] == year:
                return row["Winner"]
        return (f'{year} does not appear in the file')

year_selected = input("Select a year: ")
print(winning_team(year_selected))
