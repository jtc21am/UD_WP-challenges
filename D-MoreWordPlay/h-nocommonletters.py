# Revisiting for loops, if conditions, and using lists as storage
# [ ] What are all of the words that can be made without the letters in “AEIOSHRTN” (in other words, without the most common letters)?

#output is a list
#it is okay to use a context manager
#take into account that the list may be empty
# it is okay to convert the input words into upper case, strip

#use contect manager to open the file
#create a set for the letters that are provided in the question 
#create and empty list to hold any words that can be made without the letters provided in the question

# use a FOR loop to traverse through the word file
# create an IF statement
    # intersect the letters set with the word
    # if the resulting set is empty, add the word to the empty list of valid words

#Create another if statement to print valid word list
 # If the list is not empty, print the list (to test if empty, use len == 0)
 # Otherwise print "There are no words that can be made without AEIOSHRTN"

restricted_letters = set("AEIOSHRTN")
valid_words = []

with open('sowpods.txt') as sowpods:
    sowpods_words = [line for line in sowpods]


    for word in sowpods_words:
        amended_word = word.strip().upper()
        if not restricted_letters.intersection(amended_word):
            valid_words.append(word.strip())

if len(valid_words) != 0:
    print(valid_words)
else:
    print('There are no words that can be made without AEIOSHRTN in this text file.')




