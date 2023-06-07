#function pattern and string
# len of the pattern vs length of the words, if not equal, return false
# create a dictionary, to map the pattern and the input of the words
#add new key-values to the dictions, if the word (value) is already used, and the key is not same, return false

def match_pattern(pattern, input_str):
    pattern_map = {} 
    words = input_str.split()

    if len(pattern) != len(words):
        return False

    for i in range(len(pattern)):
        char = pattern[i]
        word = words[i]

        if char not in pattern_map:
            if word in pattern_map.values():
                return False
            pattern_map[char] = word
        
        else:
            if pattern_map[char] != word:
                return False

    return True

pattern = 'abba'
input_str = 'red blue green red'
print(match_pattern(pattern, input_str))

