'''Functions
[ ] Write a function that takes a string `prefix` as an argument and returns an array of all of the words that start with that prefix (the prefix has to be at the beginning of the word).'''

#no terminal entry as input, directly pass the prefix into the 
#First function read the file 
#function function return the words that begin with the prefix


#create a function which takes in a parameter named (text_file)
#open the text file and with list comprehension, save a list of the words in the text file line by line
#return the list to the second function so it can be used to test for the prefixes

#create a second function which takes in 2 parameters (text file and the prefix)
#create empty list to hold words
#use a for loop to iterate through the text list
#save the word being iterated as uppercase and strip the word of the new line
#use an IF statement to test if the word STARTSwith prefix (uppercase)
# append the list with the word
import sys

def read_text_file(file, prefix):
    with open(file, 'r') as textfile:
        textfile_words = [line.strip() for line in textfile]
    return prefix_in_word(textfile_words, prefix)

def prefix_in_word(textfile_words, prefix):
    words_with_prefix = []
    for word in textfile_words:
        amended_word = word.upper()
        if amended_word.startswith(prefix.upper()):
            words_with_prefix.append(word)
    print(words_with_prefix)
    
def main():
    """
    This program takes 3 command line arg forms:

    1.
    -affirm *name*

    2.
    -hello *name*

    3.
    -n *number* *name*
    """
    # standard - load "args" list with cmd-line-args
    args = sys.argv[1:]

    # args is a list of the command line argument strings that follow
    # the program.py file.
    # So if the command is: python3 affirm.py aaa bbb ccc
    # The args list  will be:
    #   args == ['aaa', 'bbb', 'ccc']
    # The args are all strings, whatever was typed in the terminal.

    # 1. Check for the -affirm arg pattern:
    #   python3 affirm.py -affirm Bart
    #   e.g. args[0] is '-affirm' and args[1] is 'Bart'
    # Select random affirmation phrase
    # Print with the name in args[1]

    if len(args) == 3 and args[0] == '-numb':
        # Note: command line values are always strings, so here
        # convert to int to pass to function.
        file = args[1]
        prefix = args[2]
        read_text_file(file, prefix)

if __name__ == '__main__':
    main()


#python3 k-function_prefix.py -numb sowpods.txt lov
    
