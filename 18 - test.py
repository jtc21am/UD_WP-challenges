'''Create and print an array containing all of the words that have a U but no other vowel.'''

#iterate through the list of words one by one
##strip the word using the method .strip to remove any foreign characters
#use a while loop and test using the following
   # Use the for loop to test each word
   # use the find method to test if the word contains a "first"
   #Create a list of the restricted vowels so then I can use them to test whether they are present
   #Use list comprehension using Any to test whether the other vowels are present
   #Create a empty list to save those words that return true
   #Print the list once we have finished testing all the words

sowpods = open('sowpods.txt','r')
word_list = [line.strip() for line in sowpods.readlines()]
restricted_letters = ["A", "E", "I", "O"]
words_with_u = []

for word in word_list:
    if word.find("U") == 1 and any([characters in word for characters in restricted_letters]) == False:
    # if word.find("U") == 1 and any([character for character in word if character in restricted_letters]):
        words_with_u.append(word)
print(words_with_u)


