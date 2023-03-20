'''For loops and if conditions
What are all of the words that have all 5 vowels, in any order?'''


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
restricted_characters = ['A', 'E', 'I', 'O', 'U']

while(word_in_list):
    if all([character in word_in_list for character in restricted_characters]) == True:
        print(word_in_list)
    word_in_list = sowpods.readline().strip()


