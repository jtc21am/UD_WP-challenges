'''For loops and if conditions
What are all of the words that both start and end with a Y?'''

# Open text file, "r" open for reading (default)
# The readlines() method returns a list containing each line in the file as a list item.
# The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters space is the default leading character to remove

# Iterate and use startswith() and endswith() methods --  to determine whether a string starts with or ends with a specific substring, respectively.
#   If both True based on "And", Print word
#   If False, move to next word list

sowpods = open("sowpods.txt","r")
rowwords = sowpods.readline().strip()

while(rowwords):
    if rowwords.startswith("Y") and rowwords.endswith("Y"):
        print(rowwords)
    rowwords = sowpods.readline().strip()