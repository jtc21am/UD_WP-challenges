'''More for loops, if conditions, and storage
[ ] What are the longest baby names in the top 40 baby names for 2020? 
Make sure you can handle if there’s a tie.'''

#open the text file as a read only
#save the baby names as a list -- .strip

#create a empty list to store the longest names
#calculate the length of the longest string of the list and save it as a variable

#for loop to iterate through the words in the list one by one
  #a nest if statement to test whether that word's length is = the variable of the longest string
  # if it is true, save the word to the (empty) list

#print list of longest words

baby_names = open('baby_names_2020_short.txt', 'r')
names_list = [line.strip() for line in baby_names]
# longest_names = []

longest_len = len(max(names_list, key=len))

longest_name = [name for name in names_list if len(name) == longest_len]
# for name in names_list:
#     if len(name) == longest_len:
    # longest_names.append(name)

print(longest_name)

baby_names.close()
