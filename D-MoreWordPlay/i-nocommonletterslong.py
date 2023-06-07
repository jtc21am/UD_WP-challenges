# Revisiting for loops, if conditions, and using lists as storage
# [ ] What is the longest word that can be made without the letters in “AEIOSHRTN” (in other words, without the most common letters)? Make sure your solution can handle ties.

#see out line by line
#it is ok to capitalize all the words as the question uses capitals
#it is ok to use a context manager
#handle the exception of empty list with a print statement

#create an empty list to store the words that satisfy the question restrictions
#Create a variable for the common letters --> str
#create a set of the str variable of the common letters
#create a variable equal to zero for the longest length

#create a context manager to open the text file and read through it line by line, saving it as a list

  #use a FOR loop to traverse through the list
    #strip and make upper case the word saving it as a new variable
    #Use IF NOT statement to intersect the set of Common letters with the word which was stripped and made uppercase
     #save a variable with length of the word
      #Use a nested If statement to test if the length > longest length variable
       #If True, longest length variable is saved as the word's length
       #Save the list as equal to the word, not add
       #If the length of the word is = to the longest length, then add the word to the list
 
 #Create an If statement to test the length of the list, if it is not 0
   #use a for loop to print each word one by one
 #Else: it is empty, print a sentence stating as such

restricted_letters_given = "AEIOSHRTN"  #MAKE THE VARIABLE NAME UPPER CASE, BC IT IS A CONSTANT VARIABLE
restricted_letter_set = set(restricted_letters_given)
common_letter_words = []
longest_length = 0

with open('sowpods.txt') as sowpods:
    sowpods_words = [line for line in sowpods]
    
    for word in sowpods_words:
        amended_word = word.strip().upper()
        if not restricted_letter_set.intersection(amended_word):
            length = len(amended_word)
            if length > longest_length:
                longest_length = length
                common_letter_words = [word.strip()]
            elif length == longest_length:
                common_letter_words.append(word.strip())

if len(common_letter_words) != 0:
    for word in common_letter_words:
        print(word)
else:
    print(f'There are no words that can be made without {restricted_letters_given} from this file.')






