'''Functions

[ ] Write a function that takes a string `substring` as an argument and returns an array of all of the words that contain that substring (the substring can appear anywhere in the word).
'''
#luke

#it is ok to use a context manager
#i do not need to validate  the user's input
# output as a list
# allow for upper or lower case matches
# Return empty list if there are no matches

#create a context manager to open the sowpods file as read only and iterate through the lines to save them in a list
# create a function which takes in as a parameter the sowpods list
# save a variable --> string which takes in the user's input of the substring.
# use list comprehension to traverse through the sowpods list and check to see if the substring is IN the word being traversed -- any valid word, save in a new list
# print new list

user_substring = input(str('Select a string to test? '))

def substring_in_word(user_substring):
    with open('sowpods.txt','r') as sowpods:
        sowpods_words = [line for line in sowpods]
        
        contains_user_substring = [] 
        for word in sowpods_words:
            if user_substring.strip().upper() in word:
                contains_user_substring.append(word.strip())
        return contains_user_substring

print(substring_in_word(user_substring))

