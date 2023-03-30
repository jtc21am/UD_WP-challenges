'''For loops and if conditions
What are all of the words that contain which has no E or A at least 15 letters long'''

# Open text file, "r" open for reading (default)
# The readlines() method returns a list containing each line in the file as a list item.
# The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters space is the default leading character to remove

# Check the length of word if greater than or equal to 15 characters long, if True   
#   Check to see whether values are not 'in' a list
#   If both True based on "And", Print word
#   If False, move to next word list

sowpods = open("sowpods.txt","r")
word_in_list = sowpods.readline().strip()

while(word_in_list):
    if len(word_in_list) >= 15:
        if "E" not in word_in_list and "A" not in word_in_list:
            print(word_in_list)
    word_in_list = sowpods.readline().strip()

sowpods.close()