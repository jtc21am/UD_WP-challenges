# Part 1

# Write code that:

# - Accepts a string (e.g. as an argument to a function, or as a command-line argument). This string represents your Scrabble “rack”.
# - Prints out the words that can be made from the characters in that input string, along with their Scrabble scores, one word per line, in descending score order

# Example input and output:

# `$ python scrabble_cheater.py SPCQEIU  # Use any language you like.`
# `17 piques`
# `17 equips`
# `16 quips`
# `16 pique`
# `16 equip`
# `15 quip`
# `…`

# create the diction for the scrabble score letters, key: letter, value: score
# read the text file

# function 1 for printing the words in score descending order (rack?, found word_list)
#   sort based on the total score of the word --> list
#   use a for loop to print the sorted words, use an f' to get the correct format
  
# function 2 calculates the score (1 word)
    # sum and a for loop using the score dictionary

# function 3 finds all iterations of the possible words (rack, word list)
#   dictionary for the rack
#   use a for loop to popoulate the dictionary and then count how many of each letter is in the rack, not the score of the letter

# possible words
# make an empty list, storing valid words that are formed
# use a for loop to iterate throuh the sowpods word list
# initialize empty dict (word_letter_count)
# for each word track of the letters in the word and the count each letter

# to test for a valid word:
#     valid_word set to True
#   loop through the letters in word_letter count,
#      compare to the dictionary for the rack, 
#         if the letter is not there, or count of the letter is greater than the rack,
#           make valid word False 
    
# if valid word true, add to the possible word list
# reutrn the list 