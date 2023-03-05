'''For loops and if conditions
[ ] What are all of the words containing an X and a Y and a Z?'''

# Open text file, "r" open for reading (default)
# The readlines() method returns a list containing each line in the file as a list item.
# The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters space is the default leading character to remove

# Create required chararcter list
# Based on a list of required characters, 
# Iterate through each character in word list, 
# Use list comprehesion to test False for any Vowel
#   All in List comprehension:
#       def any(iterable: Iterable[object], /) -> bool
#       Return True if bool(x) is True for all values x in the iterable.
#       If the iterable is empty, return True.
#   If True, print
#   If False, move to next word in list

sowpods = open("sowpods.txt","r")
word_in_list = sowpods.readline().strip()
required_characters = ["X", "Y", "Z"]

while(word_in_list):
    if all([character in word_in_list for character in required_characters]) == True:
            print(word_in_list)
    word_in_list = sowpods.readline().strip()



