'''Functions

[ ] Write a function that takes a string `word` as the first argument, a string `letter` as the second argument, and returns a count of how many times `letter` occurs in `word`.
Jessica'''

def count_letters(word, letter):
    return word.upper().count(letter.upper())

test_word = "Alphabetical"
test_letter = "a"
print(count_letters(test_word, test_letter))
