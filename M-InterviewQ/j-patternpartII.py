def match(pattern, str):
    matches = dict()  # Create an empty dictionary to store matches
    return word_match(pattern[:], str, 0, 0, matches), matches  # Call the helper function and return its result along with matches

def word_match(pattern, str, current_ptrn, str_start, matches):
    if current_ptrn == len(pattern):  # If we have reached the end of the pattern
        if str_start == len(str):  # If we have also reached the end of the input string
            return True  # Return True, indicating a successful match
        else:
            return False  # Otherwise, return False, indicating a failed match

    if pattern[current_ptrn] in matches:  # If the current pattern character is already present in matches
        for str_end in range(str_start + 1, len(str) + 1):  # Try different lengths of the substring from str_start
            if matches[pattern[current_ptrn]] == str[str_start:str_end]:  # If the substring matches the stored value for the current pattern character
                if word_match(pattern, str, current_ptrn + 1, str_end, matches):  # Recursively call _match for the next pattern character and the remaining string
                    return True  # If the recursive call returns True, propagate the success up the call stack
    else:
        for str_end in range(str_start + 1, len(str) + 1):  # Try different lengths of the substring from str_start
            matches[pattern[current_ptrn]] = str[str_start:str_end]  # Store the substring as the value for the current pattern character
            if word_match(pattern, str, current_ptrn + 1, str_end, matches):  # Recursively call _match for the next pattern character and the remaining string
                return True  # If the recursive call returns True, propagate the success up the call stack
            del matches[pattern[current_ptrn]]  # If the recursive call fails, remove the stored value for the current pattern character
    
    return False  # Return False if none of the recursive calls returned True

pattern = "abcba"
input_str = "redbluegreenbluered"

result = match(pattern, input_str)
print(result)
