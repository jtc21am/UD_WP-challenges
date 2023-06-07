# check the rack for '_' representing a wild card
# create a list of wildcards and the count of them


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
# save a new variable for the original value of wildcard

# use a for loop to iterate throuh the sowpods word list
# initialize empty dict (word_letter_count)
# for each word track of the letters in the word and the count each letter

# to test for a valid word:
#     valid_word set to True
#   loop through the letters in word_letter count,
#      compare to the dictionary for the rack, 
#         if the letter is not there AND if wildcard COUNT OF GREATER THAN OR  EQUAL COUNT is available
            if there is a value greater than 0 to the wildcard count, REDUCE THE COUNT OF WILDCARD BY THE LETTER COUNT, AND CONTINUE
                OTHERWISE make valid word False          
            if the count of the letter in the word is greater than the count of the same letter in the rack AND if the wildcard COUNT OF GREATER THAN OR EQUAL to the differnce bw letter count and rack count
                REDUCE THE COUNT OF WILDCARD BY THE difference LETTER COUNT, AND CONTINUE   
                    OTHERWISE make valid word False  
#          
    
# if valid word true, add to the possible word list
# reutrn the list 