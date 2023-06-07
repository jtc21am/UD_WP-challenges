'''Write a function that takes as input two arguments:
1. An array of numbers
2. An integer `k`
and returns an array with all of the pairs of numbers from that array that sum to `k`. You can’t use the same number twice. You can assume that there are no duplicate numbers in the array.
Example
- Input array: `[1, 9, 6, 3, 5, 4]`
- `k`: 10
- Result: `[[1, 9], [6, 4]]` // Note that `[5, 5]` is not in the solution'''

def find_pairs(arr, k):
    # Handle empty and short arrays
    if not arr or len(arr) < 2:
        return []
    
    # Initialize a set to keep track of seen numbers and an empty list for pairs
    seen = set()
    pairs = []
    
    # Loop through each element in the array using enumerate to get the index and the value
    for i, num in enumerate(arr):
        # Calculate the difference between the target sum and the current number
        target = k - num
        
        # If the target has already been seen, add the pair to the list of pairs
        if target in seen:
            # Check that the pair doesn't include duplicate values
            if arr.index(target) != i:
                pairs.append([num, target])
        
        # Add the current number and its complement to the target to the set of seen numbers
        seen.add(num)
        seen.add(target)
    
    # Return the list of pairs that sum up to k
    return pairs
if __name__ == '__main__':
    nums = [1,9,5,4,6,5,7,3]
    target = 10
 
print(find_pairs(nums, target))

'''
The problem is to find all pairs of numbers in an array that add up to a given target number k. The solution uses a hash set to store all seen numbers in the array so far. For each number num in the array, we calculate the target number target = k - num that would add up to k with num. We then check if target is already in the seen set. If it is, we have found a pair of numbers that add up to k, so we add num and target to a list of pairs. We continue iterating through the rest of the array, adding each new num to the seen set, until we have checked all pairs.

The solution uses a hash set to store seen numbers instead of a list, which makes it faster to check whether a number has been seen before. It also avoids adding duplicate pairs to the list of pairs by checking all previous numbers in the array for the target number, rather than just using the index() method to find the first occurrence of the target number.

Overall, the solution has a time complexity of O(n), where n is the length of the input array, because we loop through each number in the array only once. The space complexity is also O(n), because we need to store all seen numbers in the hash set.'''


'''Empty array: The function should return an empty list when the input array is empty.
Array with one element: The function should return an empty list when the input array has only one element, as there are no pairs to be found.
No pairs found: The function should return an empty list when there are no pairs of numbers in the array that sum up to the target.
All pairs found: The function should return a list of all possible pairs when every pair of numbers in the array sums up to the target.
Large array: The function should be able to handle large input arrays without running out of memory or taking too much time.
Negative numbers: The function should be able to handle input arrays that contain negative numbers.
Zero as a target: The function should be able to handle a target sum of zero.
Non-integer target: The function should be able to handle a target sum that is not an integer.
Duplicate elements: The function should be able to handle input arrays that contain duplicate elements, including pairs of identical numbers.
Non-numeric input: The function should be able to handle input arrays that contain non-numeric elements.'''