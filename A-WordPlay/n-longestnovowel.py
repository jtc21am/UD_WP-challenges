'''Setting up storage to use during a for loop, including counters and arrays
What is the longest word that contains no vowels?'''

# Create required chararcter list
# Based on a list of required characters, 
# Iterate through each character in word list, 
# Use list comprehesion to test False for any Vowel
#   All in List comprehension:
#       def any(iterable: Iterable[object], /) -> bool
#       Return True if bool(x) is True for all values x in the iterable.
#       If the iterable is empty, return True.
#   If True, add word to the new List
#   If False, move to next word in wordlist

# Print longest word using Max function
# longest string length using max() + key
# With a single iterable argument, return its biggest item. The default keyword-only argument specifies an object to return if the provided iterable is empty. With two or more arguments, return the largest argument.

sowpods = open("sowpods.txt","r")
word_in_list = sowpods.readline().strip()
no_vowel_list = []
restricted_characters = ['A', 'E', 'I', 'O', 'U']

while(word_in_list):
    if any([character in word_in_list for character in restricted_characters]) == False:
        no_vowel_list.append(word_in_list)
    word_in_list = sowpods.readline().strip()

print(max(no_vowel_list, key=len))
sowpods.close()