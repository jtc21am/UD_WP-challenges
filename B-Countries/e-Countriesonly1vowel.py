'''Setting up storage to use during a for loop, including counters and arrays
What countries use only one vowel in their name (the vowel can be used multiple times)
    - For example, if the word “BEEKEEPER” were a country, it would be an answer, because it only uses “E”.'''
#include Y for cases such as Rhythm
#use upper case to eliminate the need for additional search elements of lower case letters

# create an empty list to hold the words that only use one vowel
# create a set of the vowels 
# create a for loop to iterate through each country name
# create a boolean using IF, 
#     check the common elements between the set of vowels and then set of the word stripped and upper case; if the length of the common elements =1 then add the word to the empty list (or list)
# print country list

countries = open('countries.txt','r')
countries_list = []
vowels = set('AEIOUY')

for name in countries:
    if len(vowels & set(name.strip().upper())) == 1:
        countries_list.append(name.strip())
print(countries_list)

#O(N)

countries.close()