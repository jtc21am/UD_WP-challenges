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
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token in ops:
                stack.append(ops[token](operand1, operand2))
    return stack.pop()

result = evaluate_postfix_expression("1 3 4 * + 2 -")
print(result)  # Output: 11.0