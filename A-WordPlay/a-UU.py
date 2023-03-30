'''For loops and if conditions
What are all of the words containing UU?'''

# Open text file, "r" open for reading (default)
# The readlines() method returns a list containing each line in the file as a list item.
# The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters space is the default leading character to remove

# Checks to see whether a value is 'in' a list -- a “membership operator” because it checks whether a value is a member of a list.
#   If True, print
#   If False, move to next word in list

sowpods = open("sowpods.txt","r")
word_in_list = sowpods.readline().strip()

while(word_in_list):
    if "UU" in word_in_list:
        print(word_in_list)
    word_in_list = sowpods.readline().strip()

import time
print(time.perf_counter())
sowpods.close()

