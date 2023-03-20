'''What are all of the letters that never appear consecutively in an English word? For example, we know that “U” isn’t an answer, because of the word VACUUM, and we know that “A” isn’t an answer, because of “AARDVARK”, but which letters never appear consecutively?'''

# Open text file, "r" open for reading (default)
# The readlines() method returns a list containing each line in the file as a list item.
# The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters space is the default leading character to remove

# Create an array/list to store all possible alpha sets
# If:
#   Check to see whether a value is 'in' a list -- a “membership operator” because it checks whether a value is a member of a list.
#       If True, remove characters from List using the remove method
#       If False, move to next word in list
#  Print list


sowpods = open("sowpods.txt","r")
word_in_list = sowpods.readline().strip()
conseq_letters = ["AA","BB","CC","DD","EE","FF","GG","HH","II","JJ","KK","LL","MM","NN","OO","PP","QQ","RR","SS","TT","UU","VV","WW","XX","YY","ZZ"]


while (word_in_list):
    for characters in conseq_letters:
        if characters in word_in_list:
            conseq_letters.remove(characters)
    word_in_list = sowpods.readline().strip()
print(conseq_letters)