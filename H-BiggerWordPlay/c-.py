'''Bigger Wordplay Questions
[3 ] What are all of the words that have at least 3 different double letters? For example, “BOOKKEEPER” is an answer to this question because it has a double-O, a double-K, and a double-E.
Carol
'''

#create a function and iterate through the text file
# use the python library iter tools and use groupby to get a list of the each group of letters for each word (then get the length of each group of letters) BOOK  -->  B, OO, K --> 1,2,1
#use lambda to test if there are  3 or more elements in the list which are greater than 2 (pair)
# if true, print word

from itertools import groupby

def words_with_three_pairs(filename) -> str:
    with open(filename) as textfile:
        for line in textfile.readlines():
            word = line.strip()
            count_grouped_letters = ([(len(list(pair))) for key,pair in groupby(word)])
            # print(count_grouped_letters)
            if sum((map(lambda x:x>=2,count_grouped_letters))) >=3:
                print(word)

words_with_three_pairs('sowpods.txt')

