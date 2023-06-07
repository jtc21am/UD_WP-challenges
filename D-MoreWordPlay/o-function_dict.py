'''Functions
[ ] Write a function that takes a string `phrase` and returns a dictionary containing counts of how many times every character appears in `phrase`.Jessica'''
#create a function with one parameter (phrase)
#create a set of the phrase so the letters may be counted whether up case of lower case
#create an empty dictionary
#use a for loop iterating through each element in the set
#count each element and save the count in the dictionary as a key/pair value
#print dictionary

#create a variable for the phrase
#call the function(using the phrase as the arguement)

def count_elements(phrase):
    phrase_compressed = set(phrase)
    character_count = {}
    for element in phrase_compressed:
        character_count[element] = phrase.count(element)
    return character_count

print(count_elements(('Write a function that takes a string phrase.').upper()))