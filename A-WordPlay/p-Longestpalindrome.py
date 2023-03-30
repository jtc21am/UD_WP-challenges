'''Setting up storage to use during a for loop, including counters and arrays
What is the longest palindrome?'''

# Open text file, "r" open for reading (default)
# The readlines() method returns a list containing each line in the file as a list item.
# The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters space is the default leading character to remove

# Create a variable to store the longest length of a palindrome found, set to 0
# Create a variable to store a string of the a palindrome found, set as empty string

# If:
#  Word is palindrome by seeing if the word is equal to itself in reverse AND
#  Length of word is greater than the longester length variable
#    If both True
#       Save the len of palindrome in Longest length variable
#       Save the word of palindrome in String
#    If False, move to next word in list
#  Print


sowpods = open("sowpods.txt","r")
word_in_list = sowpods.readline().strip()
longest_length = 0
longest_palindrome = ""

while (word_in_list):
    if word_in_list == word_in_list[::-1] and len(word_in_list) > longest_length:
        longest_palindrome = word_in_list
        longest_length = len(word_in_list)
    word_in_list = sowpods.readline().strip()
print(longest_palindrome)

sowpods.close()