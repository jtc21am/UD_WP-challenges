'''Functions
[ ] Write a function that takes a string `word` as an argument and returns a count of all of the “A”s in that string.
Jessica'''
#create a function which takes in 1 parameters (word)
#create a variable which equals the word uppercase
# use the count method to test the occurrences of the letter A in the arguement
# return a statement ie "There are # of As in the ... word."

#create a variable for arguement "word"
#Call the function (passing the arguement 'word') and print


def contains_a(word):
    # amended_word = word.upper()
    # occurrences = word.upper().count("A")
    return word.upper().count("A")

test_word = "Alphabetical"
print(contains_a(test_word))
