'''For loops and if conditions
What country names are > 50% vowels?'''

# Ask more edgecase questions, concerned about time and space complexity, "y", correct indentation, be thoughtful when assigning names

#create a list/array of the vowels

#Create def to count the vowels
  #create a variable to store the vowel count of the word and set to zero
  #for loop to iterate through the word and use the .upper method to make all characters upper case
  #if character is in the vowel array
    #add 1 to the vowel count
    #return my vowel count

#Create a for loop to test if the count of vowels is greater than the word/2 since the challenge asks for 50%
#if true, print word
# with open('countries.txt') as countries:
#     word_in_list = [line.strip() for line in countries.readlines()]
# required_characters = ['A', 'E', 'I', 'O', 'U']

# def count_vowels(word):
#     vowel_count = 0
#     for character in word.upper():
#         if character in required_characters:
#             vowel_count += 1
#     return vowel_count

# for word in word_in_list:
#     if count_vowels(word) > (len(word)/2):
#         print(word)

# O(N*M)

# class FileHandler:
#     def __init__(self):
#         self.file = open('countries.txt','r')
#         self.lines = [line.strip().upper() for line in self.file.readlines()]

with open('countries.txt') as countries:
    word_in_list = [line.strip() for line in countries.readlines()]
required_characters = ['A', 'E', 'I', 'O', 'U']

class CountVowels:
    def __init__(self, list):
        self.list = country_names
        print(country_names)
    
    def count_vowels(self):
    vowel_count = 0
    vowels = ['A', 'E', 'I', 'O', 'U']
    for name in self.li:
        if name in vowels:
            vowel_count += 1
            print(self.vowel_count)

        if self.vowel_count > (len(name)/2):
            print(name)

fileH = CountVowels()
print(fileH.count_vowels())
countries.close()