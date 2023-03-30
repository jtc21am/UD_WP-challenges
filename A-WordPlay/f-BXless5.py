'''For loops and if conditions
What are all of the words that have a B and an X and are less than 5 letters long?'''

# Open text file, "r" open for reading (default)
# The readlines() method returns a list containing each line in the file as a list item.
# The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters space is the default leading character to remove


# Check the length of word if less than or equal to 5 characters long, and    
# Check to see whether 2 values are both 'in' a the word
#    If all True, Print word
#    If False, move to next word in list

sowpods = open("sowpods.txt","r")
rowwords = sowpods.readline().strip()

while(rowwords):
    if "B" in rowwords and "X" in rowwords and len(rowwords) <= 5:
        print(rowwords)
    rowwords = sowpods.readline().strip()

sowpods.close()


