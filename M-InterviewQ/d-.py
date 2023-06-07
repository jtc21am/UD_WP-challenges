'''Post fix'''

# import operator

# create an empty stack
# create a dictionary of the operators so i can use them later

# create a function #1 to check if the char is a valid number (operand)

# create a function #2  (parameter -> char iterated from main function, should be a operator */+-)
# to see if the stack if less than 2, if so, raise error 
#   if len greater than 2, pop 2 numbers from the stack and use the operator function to calculate, then append the subtotal to the stack.
#  if the operator is /, and 2nd # popped is ==0, raise ZeroDivisionError

#create a function to iterate through string, use split method
#   use the helper function #1 to test if it is a valid number, then add it to the stack
#   if the char is in the operator dictionary, call function #2 to pop 2 numbers off the stack and calculate the subtotal and append the subtotal to the stack
# return stack[0]

import operator

def evaluate_postfix(expr:str):
    stack = []

    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    def is_operand(char):
        return char.isdigit()

    def evaluate_operator(char): #function 2 where char is an operator such as +-*/
        if len(stack) < 2:
            raise ValueError("Invalid Expression")
        
        operand2 = stack.pop()
        operand1 = stack.pop()
        stack.append(ops[char](operand1, operand2))
    
    def evaluate_char(char):
        if is_operand(char):
            stack.append(int(char))
        elif char in ops:
            evaluate_operator(char)
        else:
            raise ValueError('invalid expression')

    for char in expr.split():
        evaluate_char(char)
    
    return stack[0]

print(evaluate_postfix("1 3 4 * + 2 -"))
print(evaluate_postfix("3 2 1 + + 2 /"))
print(evaluate_postfix("2 +"))
                        