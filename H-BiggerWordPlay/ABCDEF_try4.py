alphabet = 'abcdefghijklmnopqrstuvwxyz'

def has_unordered_alphabetic_substring(filename):
    longest = []
    length_substring = 6
    with open(filename) as textfile:
        for line in textfile.readlines():
            test_string = line.strip().lower() #O(n)
            for i in range(len(test_string)):
                for j in range(i+1, len(test_string)+1):
                    #create substring and use set to remove duplicate letters
                    substring = set(test_string[i:j])
                    #sort substring
                    sorted_substring = ''.join(sorted(substring))
                    if sorted_substring in alphabet and len(sorted_substring) >= length_substring:
                            longest.append(substring)
                            print(test_string)

has_unordered_alphabetic_substring('sowpods.txt')