# Revisiting for loops, if conditions, and using lists as storage
# [ ] What are all of the words that both start with a “TH” and end with a “TH”?

# Use line comprehension to read the content of the text, tranform the content of that text file and ouput it in to a list

# Create a funtion
# Use a for loop to iterate through each words in the outfile file
#   Save list with a statement to test whether the word begins with and end with the letters "TH" 
#   print the newly created list whihc contains words begnning and ending with "TH"

# run function
# close the text file

sowpods = open('sowpods.txt', 'r')
sowpods_words = [line.strip() for line in sowpods] 

def words_begin_end_th(output_words):
    user_defined_string = input(str('Select a string to test start and begin?: '))
    begin_end_th = [word for word in output_words if word.startswith(user_defined_string.upper()) and word.endswith(user_defined_string.upper())]
    print(begin_end_th)

words_begin_end_th(sowpods_words)
sowpods.close()