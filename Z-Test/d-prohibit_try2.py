cipher = {'a': '4', 'e': '3', 'i': '1', 'o': '0'}

def cipher_converter(string):
    # Define a lambda function that takes a character and returns its corresponding value in the cipher dictionary
    # Use map() and the lambda function to convert each character in the string
    converted = map(lambda char: cipher.get(char, char),string)
    # Join the converted characters into a new string
    result = ''.join(converted).lower()
    return result
        
def has_prohibited_words(username, prohibited_words):
    converted_prohited_words = []
    for word in prohibited_words:
        converted_prohited_words.append(cipher_converter(word))
    converted_username = (cipher_converter(username))

    return any(word in converted_username for word in converted_prohited_words)

test_prohibited_words = ['darn', 'heck']
test_username1 = 'D4RN_y0u_T0_h3ck'
test_username2 = 'good_username'
print(has_prohibited_words(test_username1, test_prohibited_words)) # Output: True
print(has_prohibited_words(test_username2, test_prohibited_words)) # Output: False

'''The cipher_converter function takes a string and uses a dictionary to convert specific characters to their corresponding value in the cipher dictionary. The function then joins the converted characters into a new string and returns it. The has_prohibited_words function takes a username and a list of prohibited words, converts them using the cipher_converter function, and then checks if any of the converted prohibited words are contained in the converted username using the any function.

Overall, the code should be able to handle the case-insensitive conversion of the prohibited words, as well as the specific letter substitutions that are specified in the problem description.'''