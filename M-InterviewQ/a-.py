#  implement a heap
# function which takes in 2 parameters the list and k

# if list empty of k zero, return empty list
# if K greater than len(list, return sorted listed in reverse)

# create heap
# use for loop
# push num to heap
# if length of heap is greater than K, pop the smallest element
# Get the k largest elements of the heap and save a variable 

# # to handle dups  check length set of the saved variable
# return sorted , reverse -> slice K

import heapq

def k_largest_numbers(nums, k):
    if not nums or k == 0:
        return []
    
    if k > len(nums):
        return sorted(nums, reverse=True)

    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    
    result=heapq.nlargest(k, heap)

    if len(result) < k:
        return sorted(nums, reverse = True)[:k]
    
    return sorted(result, reverse=True) #handle dups

nums=[5, 16, 7, 9, -1, 4, 3, 11, 2]
k=3
result = k_largest_numbers(nums,k)
print(result)