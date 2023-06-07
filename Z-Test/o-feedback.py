def longest_alpha_substring(filename):
    letter_set = set('ABCDEF')
    filled_list = []

    with open(filename) as textfile:
        for line in textfile.readlines():
            main_string = line.strip().upper()
            # Convert the main string to a set of characters
            main_set = set(main_string)
            # Check if the letter set is a subset of the main set


            if len(letter_set) <= len(main_set):
                # If the letter set is a subset of the main set, check if it appears in the main string
                for i in range(len(main_string)):

                    # print(set(main_string[i:i+len(letter_set)]),main_string)
                    if set(main_string[i:i+len(letter_set)]+1) == letter_set:
                        filled_list.append(main_string)
    print(filled_list)                                             
longest_alpha_substring('sowpods.txt')