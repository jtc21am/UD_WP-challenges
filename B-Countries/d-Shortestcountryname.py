'''Setting up storage to use during a for loop, including counters and arrays
What is the shortest country name? Make sure your solution can handle ties.'''

#Create an empty list to hold the country names that equal the shortest length
#Calculate the length of the shortest string in entire list and save it as a variable

#use a for loop to iterate through the country list
#create an If statement which tests whether the length of the word = the variable shortest_word
#If true, append the empty list to add that country name
#print the list

#Does len function count spaces? The len built-in function counts every character. That includes spaces and special characters.

import math
import time

countries = open('countries.txt','r')
word_in_list = [line.strip() for line in countries.readlines()]
shortest_word = []
smallest_len = math.inf

smallest_len = len(min(word_in_list, key=len))

for word in word_in_list:
    if len(word) == smallest_len:
        shortest_word.append(word)

print(shortest_word)

# for word in countries:
    # if len(word) == smallest_len:
    #     shortest_word.append(word.strip())
    #     smallest_len = len(word)
    # elif len(word) < smallest_len:
    #     shortest_word = []
    #     shortest_word.append(word.strip())
    #     smallest_len = len(word)

# print(shortest_word)

countries.close()