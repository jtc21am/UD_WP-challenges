def find_unordered_abcdef():
    target = set('abcdef')
    letters = set()
    substring = 'abcdefa'

    for char in substring:
        if char in target:
            letters.add(char)
        else:
            if letters != target:
                letters = set()
                
    if letters == target:
        return True


print(find_unordered_abcdef())