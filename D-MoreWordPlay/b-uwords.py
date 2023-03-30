# Revisiting for loops, if conditions, and using lists as storage
# [ ] What are all of the words that have only “U”s for vowels?

#Y is considered a vowel
#print the output one by one
#use capital U as constraint
#for loop
#set up a traditional for loop vs function

#Open the text file as read only
#Create an empty list to hold all words with U only
#Create a set which has all of the vowels including U
#use a for loop to iterate through each word in the sowpods text file one by one
#use the set intersection method to find the common elements between the vowel set and the word, 
# if the result is a U, -- Intersection returns a new set with only the common elements
# add the word to the new list
#print new list
#close the text file

# Vowels set = AEIOUY
# test_word = set(JUMP)
# Using an boolean test: Run Intersection between vowels and the test word
# Result = {U}
# Since the result is true, add the test_word to the empty list

# with open('sowpods.txt') as sowpods_file:
#     # sowpods = [(line.strip().upper() for line in sowpods_file.readlines())]
#     sowpods = sowpods_file.readlines()

with open('sowpods.txt') as sowpods:
    sowpods_words = (line.strip().upper() for line in sowpods)
    print(sowpods_words)
# vowels = set('AEIOUY')
# u_only_words = []

# for word in sowpods_words:
#     if vowels & set(word.upper()) == {'U'}:
#         u_only_words.append(word)

# for word in u_only_words:
# print(u_only_words)
# sowpods_file.close()

