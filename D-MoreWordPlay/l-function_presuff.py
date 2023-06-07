'''Functions

[ ] Write a function that takes a string `prefix` as the first argument, a string `suffix` as the second argument, and an integer `length` as the third argument. It should return an array of all of the words that start with that prefix, end with that suffix, and are that length.'''
#Saul

#empty list is ok as a return if there are no words that satifsy the requirements
#to bypass the need to test case sentive, make the arguement uppercase (then if time allows, test upper and lower case)
#count without the new line
#assume the user will pass the correct type, no validation

#create a function which takes the parameters of prefix, suffix and length
#contains_user_chocie = []
#test whether the len of prefix + suffix < length, return []
#inside the function, use list comprehesion to open the file and save a list of the words
#Use nested for loop to test whether the word begins with, ends with and is the correct length (strip the word of new line, make it upper case), also make the prefix and suffix uppercase
# If true, add the word to the list
#print the list

#call the function passing the arguements prefix, suffix, length

def pre_suff_len_in_word(prefix, suffix, length):
    word_has_pre_suff_len = []
    if (len(prefix) + len(suffix)) > length:
        return(word_has_pre_suff_len)
    else:
        with open('sowpods.txt', 'r') as sowpods:
            sowpods_words = [line for line in sowpods]
            for word in sowpods_words:
                word = word.strip().upper()

                if word.startswith(prefix.upper()) and word.endswith(suffix.upper()) and len(word) == length:
                    word_has_pre_suff_len.append(word)
            return(word_has_pre_suff_len)

print(pre_suff_len_in_word("eig", "y", 3))




