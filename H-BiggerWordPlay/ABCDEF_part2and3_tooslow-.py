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

def longest_unordered_alpha_substring(filename):
    longest_unordered_alpha_substring = []
    length_unordered_substring = 0
    with open(filename) as textfile:
        for line in textfile.readlines():
            test_word = line.strip()
            word_as_unicode_values = (list(map(int,map(ord,test_word))))

            for i in range(len(word_as_unicode_values)):
                for j in range(i+1, len(word_as_unicode_values)+1):
                    substring = word_as_unicode_values[i:j]
                    substring_sorted_set = sorted(set(substring))
                    length_substring_sorted_set = len(substring_sorted_set)
                    # print('test a',length_substring_sorted_set > length_unordered_substring)
                    if length_substring_sorted_set > length_unordered_substring:
                        if is_unordered_chain(substring_sorted_set):
                            length_unordered_substring = length_substring_sorted_set
                            longest_unordered_alpha_substring = (list(map(str,map(chr,substring_sorted_set))))
                    

        return longest_unordered_alpha_substring
    
    
def is_unordered_chain(substring_sorted_set):
    result = all(list(map(lambda x: (x[1]-x[0]) == 1, zip(substring_sorted_set, substring_sorted_set[1:]))))
    return result


print(longest_unordered_alpha_substring('sowpods.txt'))