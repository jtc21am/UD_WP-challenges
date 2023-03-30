'''Setting up storage to use during a for loop, including counters and arrays
Create and print an array containing all of the words that end in "GHTLY"'''

# Open text file, "r" open for reading (default)
# The readlines() method returns a list containing each line in the file as a list item.
# The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters space is the default leading character to remove

# Create an emtpt array/list to hold words that due satisfy the test

# Iterate and use startswith() --  to determine whether a string starts with or ends with a specific substring, respectively.
#   If both True, add word using Append method to the array/list
#   If False, move to next word list
# Print Array/list

sowpods = open("sowpods.txt","r")
word_in_list = sowpods.readline().strip()
ghtly_list =[]

while(word_in_list):
    if word_in_list.endswith("GHTLY"):
        ghtly_list.append(word_in_list)
    word_in_list = sowpods.readline().strip()
print(ghtly_list)
sowpods.close()