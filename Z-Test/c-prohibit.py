def has_prohibited_words(prohibited_words, username):
    # convert all words in prohibited_words list to lowercase and apply letter substitutions
    # so that we can do case-insensitive checks later
    prohibited_words = [word.lower().replace('a', '4').replace('e', '3').replace('i', '1').replace('o', '0') for word in prohibited_words]
    # convert the username to lowercase and apply letter substitutions
    username = username.lower().replace('a', '4').replace('e', '3').replace('i', '1').replace('o', '0')
    # check if any of the prohibited words are in the username
    for word in prohibited_words:
        if word in username:
            return True
    return False

prohibited_words = ['darn', 'heck']
username1 = 'D4RN_y0u_T0_h3ck'
username2 = 'good_username'
print(has_prohibited_words(prohibited_words, username1)) # Output: True
print(has_prohibited_words(prohibited_words, username2)) # Output: False