'''More for loops, if conditions, and storage
[ ] What is the shortest baby name in the top 40 baby names for 2020?'''


#open the text file as a read only
#create a list of the baby names
#DO NOT NEED -- create an empty list to hold the baby names that are the shortest length
#calculate the shortest length of all the words in the entire text file (use Length of shortest word (to find the shortest word in the list, use the function MIN))
# ?? if there are multiple words with min length, which does python save?? -- it returns the first encounters
#use a for loop to iterate through the list
  #create a boolean test to check if the word's length is equal to the length of the shortest word in the file, using an IF statement (Strip the word)
  #if True, add word to empty list
#print list
from time import process_time
import math

t1_start = process_time() 
#remove the 2020 from line 15

baby_names_2020 = open('baby_names_2020_short.txt', 'r')
# names_list = [line.strip() for line in baby_names_2020.readlines()]
shortest_names = []
shortest_length = math.inf


# shortest_length = len(min(baby_names_2020, key=len))
# baby_names_2020.seek(0)

# for name in baby_names_2020:
#     if len(name) == shortest_length:
#         shortest_names.append(name.strip())
# print(shortest_names)


for name in baby_names_2020:
    if len(name.strip()) < shortest_length:
        shortest_names.clear()
        shortest_names.append(name.strip())
        shortest_length = len(name.strip())
    elif len(name.strip()) == shortest_length:
        shortest_names.append(name.strip())
print(shortest_names)

t1_stop = process_time()
print(t1_stop-t1_start)
baby_names_2020.close()
