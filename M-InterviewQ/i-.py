# Output will be a boolean true or false
# check the length of the input string, bc we are verifying pairs, if the len is odd, return false
#edge case if input string empty - hold for now
# Use a stack to keep track of the opening brackets
#iterate over each char in the string
# if char is an opening bracket, push it to the stack
# if char is a closing bracket, check if it is the matching pair to the top of the stack
#   if there is a closing bracket and the stack is empty or the closing bracket and top of stack do not match, return False
# # if the pair matches, pop the top of the stack
# Iterate over all of the characters in the input, if the stack is empty and the loop is complete, return True

# if the loop is complete and the stack is not empty, return False

# Use a helper function to check the matched pairs

def check_balanced_brackets(bracket_string):
    if len(bracket_string) % 2 != 0 or len(bracket_string) == 0:
        return False
    
    stack = []
    for bracket in bracket_string:
        if bracket in '({[':
            stack.append(bracket)

        elif bracket in ')}]':
            if not stack or not is_closing_bracket_pair(stack.pop(), bracket):
                return False
    return len(stack) == 0
    

def is_closing_bracket_pair(opening, closing):
    # print(opening, closing)
    return  (opening == '(' and closing == ')') or \
            (opening == '{' and closing == '}') or \
            (opening == '[' and closing == ']')

# print(check_balanced_brackets("{[()]}"))
# print(check_balanced_brackets('{}[]()'))
# print(check_balanced_brackets('[(){()}]'))

# print(check_balanced_brackets('{}][()'))
# print(check_balanced_brackets('{[(])}'))
# print(check_balanced_brackets('[(){()}'))
# print(check_balanced_brackets('[]('))
print(check_balanced_brackets(''))

