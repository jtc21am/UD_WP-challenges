'''prohibited strings'''
#create cipher in a dictionary for the letters as key, replacements as the pair
# create cipher converter to take the string and convert it based on the dictionary
# create a function that takes the parameters of the converted username and list of prohibited words(converted the prohibited words as well).
#Check if any of the prohibited words are present in the converted username and return a boolean
# take into consideration the edgecase of empty prohibited words list
# take into consideration the edgecase of non-alphanum elements

cipher = {'a':'4', 'e':'3', 'i':'1', 'o':'0'}

def convert_char(char):
    return cipher.get(char.lower(), char)

def cipher_converter(string):
    converted_string = map(convert_char, string)
    result_joined_string = ''.join(converted_string).lower()
    return result_joined_string

def has_prohibited_words(username, prohibited_words):
    if not prohibited_words or len(username) == 0:
        return False
    
    converted_prohibited_words = [cipher_converter(word) for word in prohibited_words]
    converted_username = cipher_converter(username)

    return any(word in converted_username for word in converted_prohibited_words)

username = ['a']
prohibited_words = ['darn', 'heck']
print(has_prohibited_words(username, prohibited_words))