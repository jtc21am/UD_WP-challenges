# Write a function that takes as arguments two strings: `pattern` and `input`. Return whether or not `input` can be broken into words to match the pattern of the characters in `pattern`.

# (In other words, this is the same problem as part 1, but `input` doesn’t contain spaces, so you’ll need to determine if it is possible to split up the input into words in a way that matches `pattern`. You will likely want to use recursion.)

# | `pattern: 'abcba'`             |
# | ------------------------------ |
# | `input: 'redbluegreenbluered'` |
# | `result: True`                 |

# function 1 match pattern (pattern, input string)

# create a variable for each len of pattern and input str
# if they are both == 0, meaning empty, return True
# if one is 0, they are not the same, return False

# use a for loop to iterate through input string creating a prefix and suffix
# prefix  = input string[:i]
# suffix will be the opposite

#check if the prefix is a valid word that matches the first character in the pattern
# if valid word(prefix, pattern[index 0]):
# recursively calling function 1 updating the pattern to the next element and testing using the suffix
#     recursively call match pattern(index 1:, suffix)
#     return True


# create dictionary for characters
# how to test if valid word?
# create function 2 - named valid word (prefix, pattern[0])

# pattern: 'abcba'
# input: 'redbluegreenbluered'
# pattern i = 'a'
# prefix = 'r'
# suffix = 'edbluegreenbluered'

# validwords('r', 'a')
# pattern = 'a'
# word = 'r'

# create dictionary for characters
# iterate through range len(word)
#     if pattern[i] is not in the dictionary:
#         if word[i] in dictionary values
#             return False
#         if not add pattern[i] = word[i] to the dictionary
#     elif pattern[i] doesnt equal the word[i]
#         return False
#     return True

# def match_pattern(pattern, input_string):
#     '''test len of pattern'''


# assert match_pattern('abcba','redbluegreenbluered') == True
# assert match_pattern('aba','xxyyyxx') == True
# assert match_pattern('abba','redbluegreenred') == False

# dict = {}
# def is_valid_word(word: str, char: str) -> bool:
#     ...

# assert is_valid_word('cat','r', {}) == ({'r':'cat'}, True)
# assert is_valid_word('cat','a', {'r':'cat'}) == ({'r':'cat'}, False)
# assert is_valid_word('dog','d', {'r':'cat'}) == ({'r':'cat','d':'dog'}, True)
# assert is_valid_word('hat','r', {'r':'cat','d':'dog'}) == ({'r':'cat','d':'dog'}, False)

# # concerns - what is the range for prefix/suffix?
# # clear that key/value pair dictionary when there is a false

# what does it look like if empty?
# what does it look it if the input is 1 char?
# then 2, then 3, 

def can_match_pattern(pattern, input_str):
    # If both pattern and input_str are empty, return True
    if len(pattern) == 0 and len(input_str) == 0:
        return True

    #  If either pattern or input_str is empty but not both, return False
    if len(pattern) == 0 or len(input_str) == 0:
        return False

    # Iterate through different possible prefix lengths of input_str
    for i in range(1, len(input_str)):
        # Split input_str into prefix and suffix
        prefix = input_str[:i]
        suffix = input_str[i:]

        # Check if prefix is a valid word that matches the first character in pattern
        if is_valid_word(prefix, pattern[0]):
            # Recursively call can_match_pattern with updated pattern and remaining suffix
            if can_match_pattern(pattern[1:], suffix):
                return True

    # No valid match found, return False
    return False

char_map = {}
def is_valid_word(word, char):
    for i in range(len(word)):
        if char not in char_map:
            if word[i] in char_map.values():
                return False
            else:
                char_map[char] = word
                return True
        else:
            # if char in char_map:
            if word[i] not in char_map.values():
                return False
            else:
                return True
            
pattern = 'abcba'
input_str = 'redbluegreenbluered'
print(can_match_pattern(pattern, input_str))

            
            