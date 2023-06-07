#no blank strings

def longest_alpha_substring(filename):
    longest_substring = []
    len_sub = 0

    with open(filename) as textfile:
        for line in textfile.readlines():
            s = line.strip().upper()
            if len(line) < len(longest_substring):
                pass
            word = (list(map(int,map(ord,s))))

            for i in range(len(word)):
                for j in range(i+1, len(word)+1):
                    love = word[i:j]
                    love_set = sorted(set(love))
                    result = all(list(map(lambda x: (x[1] - x[0]) == 1, zip(love_set, love_set[1:]))))
                    
                    if result == True:
                        if len(love_set) > len_sub:
                            len_sub = len(love_set)
                            longest_substring = (list(map(str,map(chr,love_set))))

# zip(my_list, my_list[1:]) creates pairs of adjacent elements in the list. For example, [(1, 3), (3, 6), (6, 8), (8, 10)].
# lambda x: abs(x[1] - x[0]) == 1 defines a function that takes a pair of adjacent elements and checks if they are 1 digit apart.
# map applies the lambda function to each pair of adjacent elements in the list.
# list converts the resulting map object to a list.
# result is a list of boolean values indicating whether each adjacent pair is 1 digit apart.
                    
                    
        return(longest_substring)


print(longest_alpha_substring('sowpods.txt'))