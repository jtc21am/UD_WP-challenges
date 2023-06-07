''' Python3 code for k largest elements in an array'''

# def kLargest(arr, k):
#     # Sort the given array arr in reverse
#     # order.
#     arr.sort(reverse=True)
#     # Print the first kth largest elements
#     for i in range(k):
#         print(arr[i], end=" ")
 
 
# # Driver code
# arr = [1, 23, 12, 9, 30, 2, 50]
# # n = len(arr)
# k = 3
# kLargest(arr, k)



# import heapq

# def find_k_largest(nums, k):
#     """
#     Finds the k largest integers in a list using the heapq module.
#     """
#     largest_nums = (sorted(heapq.nlargest(k, nums), reverse=True))
#     return largest_nums
# # Example usage:
# nums = [4, 2, 8, 1, 5, 9, 3]
# k = 3
# print(find_k_largest(nums, k))


import heapq

def k_largest_numbers(nums, k):
    if not nums or k==0:
        return []  # Handle empty input, Handle k = 0
    
    if k > len(nums):
        return sorted(nums, reverse=True)  # Handle k > len(nums)
    
    heap = [] # initialize the heap
    for num in nums:
        heapq.heappush(heap, num)  # Push num to heap
        if len(heap) > k:  # Remove smallest element from heap, if len(heap is greater than k)
            heapq.heappop(heap)
    
    result = heapq.nlargest(k, heap) # Get k largest elements from heap
    
    if len(result) < k:
        return sorted(nums, reverse=True)[:k]  # Handle k > len(set(nums))
    
    return sorted(result, reverse=True)  # Handle duplicates

# Example usage
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
k = 4

result = k_largest_numbers(nums, k)
print(result)  # Output: [6, 5, 5, 5]
