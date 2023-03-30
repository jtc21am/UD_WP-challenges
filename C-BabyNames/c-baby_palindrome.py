'''Nested for loops
[ ] There is at least one baby name from the top 40 baby names for 2020 that, when spelled backwards, is a valid Scrabble word. Find and print all such names.
Solve this two ways: 
first with an array to hold the Scrabble words, 
and then with a dictionary (or set) to hold the Scrabble words. 
Use timer functions to measure how long it takes to complete this work under each implementation. Why is the time different?'''


#at least one -- meaning that there could be more than one valid response
#to ensure valid boolean response and to elimante the need for a 3rd for loop to test lower case vs. upper case
#if multiples, still add to new valid response list



# open the sowpods txt file and save the words into a list
# open the baby name txt file
# create an empty list to hold valid baby names
# a word in reverse order that is a valid word is considered a "palidrome", and I can use the ::-1 method
# run a for loop through each baby name, strip the word of extra characters, make it upper case
#   then use an IF statement to test whether the name(reversed) is equal to a word in the saved sowpods word list 
#   If true, save the name -- into a new valid name list
# print the list of the valid baby name
# run a timer -- by importing time, then using .perf_counter to check the run speed
# close the text files

# baby_names = open('baby_names_2020_short.txt','r')  --> "baby_names" is a file object

from time import perf_counter

time_start = perf_counter()

# with open('sowpods.txt') as sowpods:
#     sowpords_list = [line.strip().upper() for line in sowpods.readlines()]

# baby_names = open('baby_names_2020_short.txt','r')

# valid_reversed_names = [name.strip() for name in baby_names if name.strip().upper()[::-1] in sowpords_list]

# print(valid_reversed_names)

# time_stop = perf_counter()
# print(time_stop-time_start)

# baby_names.close()


#USING NESTED LOOPS AND SETS
with open('sowpods.txt') as sowpods:
    sowpords_list = set(line.strip().upper() for line in sowpods.readlines())

with open('baby_names_2020_short.txt') as baby_names:
    baby_names_list = set(line.strip().upper() for line in baby_names.readlines())

valid_reversed_names = [name.strip() for name in baby_names_list if name.strip().upper()[::-1] in sowpords_list]

print(valid_reversed_names)
time_stop = perf_counter()
print(time_stop-time_start)



