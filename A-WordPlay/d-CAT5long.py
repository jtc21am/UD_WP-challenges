'''For loops and if conditions
What are all of the words that contain the word CAT and are exactly 5 letters long'''

# Open text file, "r" open for reading (default)
# The readlines() method returns a list containing each line in the file as a list item.
# The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters space is the default leading character to remove

# Check the lenggth of word if = 5 and   
# whether a value is 'in' a list -- a “membership operator” because it checks whether a value is a member of a list.
#   If both are True, print word
#   If False, move to next word list

sowpods = open("sowpods.txt","r")
rowwords = sowpods.readline().strip()

while(rowwords):
    if len(rowwords) == 5 and "CAT" in rowwords:
        print(rowwords)
    rowwords = sowpods.readline().strip()
