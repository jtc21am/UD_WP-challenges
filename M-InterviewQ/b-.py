#if it list is empty or there are less than 2 elements in the list, return empty []
# create an empty set for seen elements, and an empty list for pairs found
# loop through each element in the list
#calculate the target to be K-element
# if the target is in the seen set, I have found a pair of numbers that add up to k
# loop through the previous numbers, if I find it, add it to the pair list

# add the element to the seen set

# return the pairs

def find_pairs(list_numbers, k):
    # if not list_numbers or len(list_numbers) < 2:
    #     return []
    
    seen_set = set()
    pairs_found = []

    for i, num in enumerate(list_numbers):
        target = k - num

        if target in seen_set:
            for j in range(i):
                if list_numbers[j] == target:
                    pairs_found.append([num, target])
                    break

        seen_set.add(num)
        print(seen_set)
    
    return pairs_found

# if __name__ == 'main':
list_numbers = [1, 9, 6, 3, 5, 4]
k = 10

print(find_pairs(list_numbers, k))

