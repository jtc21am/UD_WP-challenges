import operator

def evaluate_postfix_expression(expr: str) -> float:
    stack = []  # Stack to store intermediate results
    
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }

    def is_operand(token):
        # Check if the token is a valid operand (number)
        return token.isdigit() or (token.startswith('-') or token.startswith('+')) and token[1:].isdigit()

    def evaluate_operator(token):
        # Evaluate an operator by popping operands from the stack
        if len(stack) < 2:
            raise ValueError("Invalid Expression: Missing operand(s).")

        operand2 = stack.pop()
        operand1 = stack.pop()
        if token == '/' and operand2 == 0:
            raise ZeroDivisionError("Division by zero.")
        else:
            stack.append(ops[token](operand1, operand2))

    def evaluate_token(token):
        # Evaluate a token based on its type (operand or operator)
        if is_operand(token):
            stack.append(float(token))
        elif token in ops:
            evaluate_operator(token)
        else:
            raise ValueError(f"Invalid Expression: '{token}' is not a valid operator or operand.")

    for token in expr.split():
        evaluate_token(token)

    if len(stack) != 1:
        raise ValueError("Invalid Expression: Extra operand(s).")

    return stack[0]

result = evaluate_postfix_expression("1 3 4 * + 2 -")
print(result)
