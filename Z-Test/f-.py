
def isValid(s):
    if len(s) % 2 != 0:
        return False
    
    stack = []
    matched_pairs = {'(':')', '{':'}','[':']'}
   
    for char in s:
        if char in {'(', '{', '['}:
            stack.append(char)
        elif char in {')', '}', ']'}:
            if not stack or matched_pairs[stack.pop()] != char:
                return False
    
    return len(stack) == 0

s1 = '[(){()}]'
s2 = '[({'
print(isValid(s1))
print(isValid(s2))