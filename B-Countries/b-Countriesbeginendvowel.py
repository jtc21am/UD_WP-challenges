'''For loops and if conditions
What countries both begin and end with a vowel?'''

# Open text file, "r" open for reading (default)
# The readlines() method returns a list containing each line in the file as a list item.
# The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters space is the default leading character to remove

# Create required chararcter list
# Based on a list of required characters, 
# Iterate through each character in word list, 
# Use list comprehesion to test False for any Vowel
#   Any in List comprehension:
#       def any(iterable: Iterable[object], /) -> bool
#       Return True if bool(x) is True for any x in the iterable.
#       If the iterable is empty, return False.
#   If True, print
#   If False, move to next word in list

countries = open('countries.txt','r')
word_in_list = [line.strip() for line in countries.readlines()]
required_characters = ['A', 'E', 'I', 'O', 'U']


for word in word_in_list:
    if word.startswith(tuple(required_characters)) and word.upper().endswith(tuple(required_characters)):
        print(word)
countries.close()