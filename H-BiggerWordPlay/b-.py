'''Bigger Wordplay Questions

[ ] What are all of the words that are at least 8 letters long and use 3 or fewer different letters? For example, “REFERRER” is an answer to this question, because it uses only 3 different letters: R, E, and F.
Sara'''
# output is ok to be a list
#test the length of the word to ensure it is greater than or equal to 8, and check if the length of word's set is fewer than 3
# # if it's true, add to a list, and print after looping through all the words

def eight_letter_words(filename) ->list[str]:
    with open(filename) as textfile:
      
        print([line.strip() for line in textfile.readlines() if test(line.strip())])
   
        """use helper function"""
def test(line):
    return len(set(line)) <=3 and len(line) >=8

eight_letter_words('sowpods.txt')