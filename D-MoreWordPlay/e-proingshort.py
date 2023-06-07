'''Revisiting for loops, if conditions, and using lists as storage
[ ] What are the shortest words that start with “PRO” and end in “ING”? Make sure your solution can handle ties.'''

'''More for loops, if conditions, and storage
[ ] What is the shortest baby name in the top 40 baby names for 2020?'''

#import math
#open sowpods file, as read only
#Create a variable shortestlength and set it equal to math.inf
#create an empty list to save the words that the shortest and begin "pro" and end with "ing"

#create a for loop to iterate through the sowpods text file
# create a variable for the word we are iterating through, strip the word and make it upper case
# Create nested if statement word begins with PRO and ends with ING:
#if (len) word < shortest length
  #shortest_length = length of the word
  #clear the list of shortest words, and then add the word to the list
#elif length word == shortest word
  # add the word to the list
#print list
#close file

import math
sowpods = open('sowpods.txt','r')
shortest_length = math.inf
shortest_words = []

for word in sowpods:
    word = word.strip().upper()
    if word.startswith("PRO") and word.endswith("ING"):
        length_word = len(word)
        if length_word < shortest_length:
            shortest_length = length_word
            shortest_words = [word]
        elif length_word == shortest_length:
            shortest_words.append(word)
print(shortest_words)
sowpods.close()
