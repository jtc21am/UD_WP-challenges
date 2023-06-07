'''Bigger Wordplay Questions
[ 4] Write a function that takes a string `availableLetters` as an argument and returns an array of all of the words that can be made from only those letters. Letters can be re-used as many times as needed and can appear in any order. Not all of the letters in `availableLetters` have to be used.
luke
'''
#output will be a list of words
# inputs will be the filename of the textfile and a string
# make the inputted string a set (uppsercase)
# use a helper function test if the string is a superset of the word in the list of words
# print the word if the helper function is true

def read_text_file(filename, input_string):
    with open(filename) as textfile:
        print([word.strip() for word in textfile.readlines() if test_word_characters(word.strip(), input_string.upper())])

def test_word_characters(word, input_string):
    letters_required = set(input_string)
    return letters_required.issuperset(word)

read_text_file('sowpods.txt', 'CDEFGHI')