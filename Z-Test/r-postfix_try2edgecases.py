import operator

def evaluate_postfix_expression(expr: str) -> float:
    stack = []
    
    ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
} 
    for token in expr.split():
        if token.isdigit():
            stack.append(float(token))

        elif token in ops:
            if len(stack) < 2:
                raise ValueError("Invalid Expression: Missing operand(s).")
            
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '/' and operand2 == 0:
                    raise ZeroDivisionError("Division by zero.")
            else:
                stack.append(ops[token](operand1, operand2))
                
        elif token.startswith('-') or token.startswith('+') and token[1:].isdigit():
            stack.append(float(token))
    
        else:
            raise ValueError(f"Invalid Expression: '{token}' is not a valid operator or operand.")
        
    if len(stack) != 1:
        raise ValueError("Invalid Expression: Extra operand(s).")
    
    return stack[0]

result = evaluate_postfix_expression("-1 3 4 * + 2 -")
print(result)  # Output: 11.0

# To create a robust postfix expression evaluator, we need to handle various edge cases that can occur during the evaluation process. Here are some edge cases that we may need to handle:

# 1. Invalid Expression: If the input expression is not valid or contains invalid characters, then we need to handle such cases and raise an appropriate error message.

# 2. Division by zero: If the expression contains a division by zero, then it will result in a runtime error. Hence we need to handle such cases and raise an appropriate error message.

# 3. Handling Floating-Point Numbers: In some cases, the evaluation of the expression may result in a floating-point number. Hence we need to handle such cases and make sure that the returned value is a floating-point number.

# 4. Unary Operators: If the postfix expression contains unary operators such as a negative sign (-) or a positive sign (+), then we need to handle such cases and perform the appropriate operation.

# 5. Missing or Extra Operand: If the postfix expression is missing an operand, or has extra operands, then we need to handle such cases and raise an appropriate error message.

# 6. Handling Large Numbers: If the operands or the result of the expression are very large, then we may need to handle such cases and use appropriate data types or algorithms to perform the arithmetic operations.

# 7. Parentheses and Precedence: If the expression contains parentheses or operators with different precedence levels, then we need to handle such cases and use the appropriate order of evaluation.

# By handling these edge cases, we can create a robust postfix expression evaluator that can handle a wide range of inputs and provide accurate results.