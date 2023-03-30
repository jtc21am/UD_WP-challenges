'''Setting up storage to use during a for loop, including counters and arrays
 Which of the letters Q, X, and Z is the least common?'''

# Open text file, "r" open for reading (default)
# The readlines() method returns a list containing each line in the file as a list item.
# The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters space is the default leading character to remove

# Create required chararcter list
# Create dictionary to store key value pair of letter and the count, set count at 0
# If character appears as key in Dictionary, increment the count

# Print key with smallest value in dictionary using Min function
# With a single iterable argument, return its smallest item. The default keyword-only argument specifies an object to return if the provided iterable is empty. With two or more arguments, return the smallest argument.

sowpods = open("sowpods.txt","r")
word_in_list = sowpods.readline().strip()
required_characters = ['Q','X','Z']
qxz_dict = {'Q':0,'X':0,'Z':0}


while(word_in_list):
    for character in word_in_list:
        if character in required_characters:
            qxz_dict[character] += 1     
    word_in_list = sowpods.readline().strip()

print(min(qxz_dict))

#min_value = min(qxz_dict)
#min_value_letter = min(qxz_dict.values())
sowpods.close()