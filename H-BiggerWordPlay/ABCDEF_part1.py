'''Bigger Wordplay Questions

[ ] Finding alphabet chains:
    - First, what are all of the words that have a least one “A”, one “B”, one “C”, one “D”, one “E”, and one “F” in them, in any order?
        - For example, “FEEDBACK” is an answer to this question
    - Next, is “ABCDEF” the longest alphabet chain that can be found in a word, or is there a longer chain starting somewhere else in the alphabet? Find the longest chain and the words that can be made from that chain.'''

#create an empty list to hold valid words

# #loop through the sowpods list by word
# create an empty set which holds a string's letters that also exist in the alpha chain

# #check the length of the word, if the length is less than the length of the alphabet chain, skip it
# iterate through each word by index and check if it is equal to an element in the alphabet chain, 
# if it is in the alpha chain set: add it to the new set, check the new set to see if the new set = target set, add word to a new list of valid words
# if it is not in the alpha chain set, clear the new set and continue the loop

# print(valid word list)

#call function

def longest_alpha_substring(test_string):
    target_alpha = test_string
    target_alpha_set = set(target_alpha)
    words_with_target_alpha = []

    with open('sowpods.txt') as textfile:
        for line in textfile.readlines():
            alpha_letters_found = set()
            test_word_alpha = line.upper().strip()
            if len(test_word_alpha) < len(target_alpha):
                pass

            for char in test_word_alpha:
                if char in target_alpha_set:
                    alpha_letters_found.add(char)

                    if alpha_letters_found == target_alpha_set:
                        words_with_target_alpha.append(test_word_alpha)
                
                else:
                    alpha_letters_found.clear()

        print(words_with_target_alpha)

   

           





# # set (string[i:i+len(alpha_chain)]) -- do not consider duplicates 
# # if it is equal, add to a list

# def longest_alpha_substring(filename):
#     letter_set = set('ABCDEF')
#     len_letter_set = len(letter_set)
#     words_with_alpha_substrings = []

#     with open(filename) as textfile:
#         for line in textfile.readlines():
#             main_string = line.strip().upper()

#             main_set = set(main_string)
#             len_main_set = len(main_set)
           
#             if len_letter_set <= len_main_set:
#                 for i in range(len(main_string)):
#                     if set(main_string[i:i+len_letter_set+1]) == letter_set:
#                             words_with_alpha_substrings.append(main_string)   
#     return(words_with_alpha_substrings)

# print(longest_alpha_substring('sowpods.txt'))

# 'wabcdefl'
# wabcdefl

#kefdbacn



