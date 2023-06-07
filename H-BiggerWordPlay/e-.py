'''Bigger Wordplay Questions
[5 ] What are all of the compound words? These are words made up of 2 smaller words. For example, “SNOWMAN” is a compound word made from “SNOW” and “MAN”, and “BEACHBALL” is a compound word made from “BEACH” and “BALL”.'''

#open the text file, save the list of words as set
#output a list of compound words, limit to 2 words only
#loop through all of the words in the text file
# loop through each indicees beginning with the 2nd element, range will be 1 through the end of the word which is calulated by the length of the word.  i.e. if string is 'snowman'--> N-O-W-M-A-N   
#   if characters to the left of the index are a valid word AND, the characters to the right of the index are also a valid word, add the WORD itself to a new list of VALID compound words.

def findallcompoundwords(filename) -> list[str]:
    with open(filename) as textfile:
        words = [line.upper().strip() for line in textfile]
        wordset = set(words)
    
    return [word for word in words if iscompound(word, wordset)]

def iscompound(word, wordset):
    for i in range(1, len(word)):
        if word[:i] in wordset and word[i:] in wordset:
            return True
        
    
print(findallcompoundwords('sowpods.txt'))