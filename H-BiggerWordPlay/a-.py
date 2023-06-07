'''Bigger Wordplay Questions
[ ] What is the longest word where no letter is used more than once?
Jessica'''
# docstrings and type strings

def find_longest_no_dups_words(filename):
    longest_length = 0
    longest_words = []
    with open(filename) as sowpods:
        for line in sowpods.readlines():
            word = line.strip()
            len_set_word = len(set(word))
            len_word = len(word)
            if len_word == len_set_word:
                if len_word > longest_length:
                    longest_words = [word]
                    longest_length = len_word
                else:
                    if len_word == longest_length:
                        longest_words.append(word)
  
    print(longest_words)
find_longest_no_dups_words('sowpods.txt')
