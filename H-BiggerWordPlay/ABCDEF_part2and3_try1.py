'''Bigger Wordplay Questions

[ ] Finding alphabet chains:
    - First, what are all of the words that have a least one “A”, one “B”, one “C”, one “D”, one “E”, and one “F” in them, in any order?
        - For example, “FEEDBACK” is an answer to this question
    - Next, is “ABCDEF” the longest alphabet chain that can be found in a word, or is there a longer chain starting somewhere else in the alphabet? Find the longest chain and the words that can be made from that chain.'''

#cabled - no wrap around
#empty list for longest substring
#variable for length of longest current chain =0

#Function#1
#add refactor for length after code works
#open text.. sowpods
# map the (word for sowpods) string, using ORD into a list
# loop through the indicees by range of string -->i
#create a nested loop by range of range(range will be (i+1, (len(string+1)))) --> j
#create a substring of the string using slice [i:j]
# create a set of the substring, sorted
#save the length sorted substring set --do not consider duplicates

#if #line 26 true AND length sorted sub set > longest current chain THEN save this string as longest current chain
# return function2(sorted ord list)

#Function 2(substring_set) -->is_unordered_chain
# ALL (map, use lambdax[1] -x[0]==1, zip(pair) -- if all Return boolean answer, 

import sys
from ABCDEF_part1 import *

def longest_unordered_alpha_substring(filename):
    longest_unordered_alpha_substring = []
    length_current_longest_substring = 5
    with open(filename) as textfile:
        for line in textfile.readlines():
            test_word = line.strip()

            word_as_unicode_values = list(map(int,map(ord,test_word)))

            for i in range(len(word_as_unicode_values)):
                for j in range(i+1, len(word_as_unicode_values)+1):
                    substring = word_as_unicode_values[i:j]
                    substring_no_dups = set(substring)
                    length_substring_no_dups = len(substring_no_dups)

                    if length_substring_no_dups > length_current_longest_substring:
                        if is_unordered_chain(substring_no_dups,length_substring_no_dups):
                            length_current_longest_substring = length_substring_no_dups
                            longest_unordered_alpha_substring = list(map(str,map(chr,substring_no_dups)))

        return longest_unordered_alpha_substring
    
def is_unordered_chain(substring_no_dups,length_substring_no_dups):
    is_substring_chain_list = list(map(lambda x: x - (min(substring_no_dups)-1), substring_no_dups))
    result = length_substring_no_dups == max(is_substring_chain_list) - min(is_substring_chain_list) + 1
    return result

longest_unordered_alpha_substring('sowpods.txt')

words = longest_alpha_substring(longest_unordered_alpha_substring('sowpods.txt'))


# 1. Check that the list is not empty and contains at least two elements.
# 2. Find the smallest element in the list.
# 3. Subtract 1 from the smallest element to get the offset.
# 4. Subtract the offset from each element in the list.
# 5. Check that all elements in the list are positive.
# 6. Find the largest element in the adjusted list.
# 7. Calculate the number of elements in the list using the formula n = largest - smallest + 1.
# 8. Check that the number of elements in the list is equal to the length of the list.
# 9. If the number of elements in the list is equal to the length of the list, then the original list is a continuous sequence.
# 10. If the number of elements in the list is not equal to the length of the list, then the original list is not a continuous sequence.

# For example, let's consider the unordered list [7, 10, 8, 9, 11].
# 1. The list is not empty and contains at least two elements, so we can proceed to step 2.
# 2. The smallest element in the list is 7.
# 3. Subtracting 1 from 7 gives an offset of 6.
# 4. Subtracting the offset from each element in the list gives the adjusted list [1, 4, 2, 3, 5].
# 5. All elements in the adjusted list are positive.
# 6. The largest element in the adjusted list is 5.
# 7. The number of elements in the adjusted list is n = 5 - 1 + 1 = 5.
# 8. The length of the original list is also 5.
# 9. Since the number of elements in the adjusted list is equal to the length of the original list, we can conclude that the original list [7, 10, 8, 9, 11] is a continuous sequence.
# 10. If the number of elements in the adjusted list was not equal to the length of the original list, then we would conclude that the original list is not a continuous sequence.
