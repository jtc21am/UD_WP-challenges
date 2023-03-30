'''For loops and if conditions
What are all of the countries that have “United” in the name?'''

# Open text file, "r" open for reading (default)
# Create array using list comprehension 
# The readlines() method returns a list containing each line in the file as a list item.
# The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters space is the default leading character to remove


# Check whether a value is 'in' an array -- a “membership operator” because it checks whether a value is a member of a list.
#   If both are True, Print word
#   If False, move to next word


countries = open('countries.txt','r')
word_list = [line.strip() for line in countries.readlines()]

for word in word_list:
    if "United" in word:
        print(word)
countries.close()