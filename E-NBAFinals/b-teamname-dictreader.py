'''Read the NBA finals CSV data into one more more data structures as needed to complete the following:
[ ] Write a function that takes as an argument a team name and returns an array of all of the years the team has won the NBA finals.
Carol'''

#print the list as one long list
# return an error if the team name does not appear
# ok to check in upper case, but return the original name 

#import csv
# create a function which takes in one parameter - string
# create an empty list to hold the years the team won
#use list comprehension to read the cvs file and save it
#use a For loop to iterate through each row
# use an if statement to check if Name of NBA team (upper case)== user selected name (upper case)
# if true add the year to the list
#if no matches, return an error statement

#return the list

# create a variable which prompts user for NBA team name
# call the function (pass the arguement variable) and print 

import csv

def winning_years(team: str) -> list:
    years_won = []
    with open('nba_finals.csv') as csvfile:
        nba_reader = csv.DictReader(csvfile)
        for row in nba_reader:
            if row["Winner"].upper() == team.upper():
                years_won.append(row['Year'])
        return years_won

team_selected = input("Select an NBA team: ")
print(winning_years(team_selected))
