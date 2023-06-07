def longest_unordered_alphabetic_substring():
    # with open(filename) as textfile:
    #     for line in textfile.readlines():
    s = 'nueregfdback'
    test_string = s.strip().lower()
    n = len(s)
    
    # Compute two arrays inc and dec of length n
    # inc[i] stores the length of the longest increasing subsequence ending at index i
    # dec[i] stores the length of the longest decreasing subsequence starting at index i
    inc = [1] * n
    dec = [1] * n
    
    # Compute increasing
    for i in range(1, n):
        for j in range(i):
            if s[j] < s[i]:
                inc[i] = max(inc[i], inc[j] + 1)
    
    # Compute decreasing
    for i in range(n-2, -1, -1):
        for j in range(n-1, i, -1):
            if s[j] < s[i]:
                dec[i] = max(dec[i], dec[j] + 1)
    
    # Find the maximum sum of inc[i] and dec[i] - 1 for all indices i
    max_sum = 0
    for i in range(n):
        max_sum = max(max_sum, inc[i] + dec[i] - 1)
    
    # Find the longest unordered alphabetic substring that includes the letter at index i
    result = ''
    for i in range(n):
        if inc[i] + dec[i] - 1 == max_sum:
            subseq = s[i - inc[i] + 1:i + dec[i]]
            sorted_subseq = ''.join(sorted(subseq))
            if sorted_subseq == subseq:
                if len(subseq) > len(result):
                    result = subseq
    
    return result
   
print(longest_unordered_alphabetic_substring())

'''The line for i in range(n-2, -1, -1) is a for loop that iterates over a range of indices starting from n-2 and ending at -1, in reverse order with a step size of -1. Here's what each of these parameters means:

n-2 specifies the starting index of the range. We use n-2 instead of n-1 because we want to iterate over all the indices of the dec array except the last one (since there are no decreasing subsequences that end at the last index).
-1 specifies the ending index of the range. We use -1 because we want to iterate over all the indices of the dec array in reverse order, starting from the second-to-last index and ending at the first index (since the last index is already covered by the inc array).
-1 specifies the step size of the range. We use -1 because we want to iterate over the range in reverse order.
By iterating over the dec array in reverse order, we can compute the lengths of the longest decreasing subsequences starting at each index. This is because, to compute the length of the longest decreasing subsequence starting at index i, we need to look at the elements to the right of index i in reverse order (i.e., from n-1 down to i+1) and see which ones are smaller than s[i]. This is why we use a reverse loop that starts from n-2 (which is the second-to-last index of dec) and ends at 0 (which is the first index of dec).'''
