'''For loops and if conditions
What are all of the words containing a Q but not a U?'''

# Open text file, "r" open for reading (default)
# The readlines() method returns a list containing each line in the file as a list item.
# The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters space is the default leading character to remove

# Checks to see whether a value is 'in' a list -- a “membership operator” because it checks whether a value is a member of a list.
# Iterate through each character in word, test if 'Q' exists and not 'U'
#   If both True, print
#   If False, move to next word in list

sowpods = open("sowpods.txt","r")
word_in_list = sowpods.readline().strip()

while(word_in_list):
    if "Q" in word_in_list and not "U" in word_in_list:
        print(word_in_list)
    word_in_list = sowpods.readline().strip()
sowpods.close()