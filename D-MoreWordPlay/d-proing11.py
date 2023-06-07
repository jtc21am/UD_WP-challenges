'''Revisiting for loops, if conditions, and using lists as storage
[ ] What are all of the words that start with “PRO”, end in “ING”, and are exactly 11 letters long?'''
#output in a list
#sowpods file content is in upper case
#use a for loop to begin

#open the data file so it may be used and designate to read only
#create an empty to hold all the words which satisfy the question requirements
#create a for loop to iterate through the text file
#modify the word being itereated to remove the new line characters
#  nested IF statement:
#    within the same IF statement use AND to check the length of the word
#    to test whether the word begins with PRO, ends with ING,
#  If True, add the word to the newly created list to store
#Print list of words that are True
#Close the text file

pro_ing_11 = []
# sowpods = open('sowpods.txt', 'r')
with open('sowpods.txt', 'r') as sowpods:
    for word in sowpods:
        word = word.strip()
        if len(word) == 11 and word.startswith('PRO') and word.endswith('ING'):
            pro_ing_11.append(word)
print(pro_ing_11)
# sowpods.close()

