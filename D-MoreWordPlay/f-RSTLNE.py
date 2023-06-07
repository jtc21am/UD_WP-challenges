# Revisiting for loops, if conditions, and using lists as storage
# [ ] What are all of the words that can be made from only the letters in “RSTLNE”? Not all of those letters need to be used, and letters can be repeated.

#context manager to open the file and use a for loop to create a set of the words from the text file

#create a set of the possible letters
#create an empty list to hold the words that satisfy the subsequent test, 
#create a for loop to iterate through the set of words

#  use a nested IF statement to test whether all the letters required are in the word (use the superset method)
#    If True, add word to the list
#print the list

with open('sowpods.txt', 'r') as sowpods:
    sowpods_words = [line.strip() for line in sowpods]  #O(N)
letters_required = set("RSTLNE")
valid_words = []

for word in sowpods_words:
    if letters_required.issuperset(word):
        valid_words.append(word)
print(valid_words)

