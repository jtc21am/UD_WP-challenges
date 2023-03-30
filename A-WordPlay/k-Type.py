'''Setting up storage to use during a for loop, including counters and arrays
How many words contain the substring "TYPE”?'''

# Open text file, "r" open for reading (default)
# The readlines() method returns a list containing each line in the file as a list item.
# The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters space is the default leading character to remove

# Set a counter to zero
# Iterate to check whether a value Type is 'in' a list -- a “membership operator” because it checks whether a value is a member of a list.
#   If True, add 1 to counter
#   If false, move to next word

sowpods = open("sowpods.txt","r")
word_in_list = sowpods.readline().strip()

count=0
while (word_in_list):
    if "TYPE" in word_in_list:
        count += 1
    word_in_list = sowpods.readline().strip()
print(count)

import time
print(time.perf_counter())
sowpods.close()