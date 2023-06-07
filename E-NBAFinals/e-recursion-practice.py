'''Read the NBA finals CSV data into one more more data structures as needed to complete the following:
[ ] Print out a ranking of who has won the MVP more than once, by times won, e.g. this output:
    - 6 times: Michael Jordan
    - 3 times: Shaquille O'Neal, LeBron James
    - 2 times: <etc>
Ryan'''

def factorial(x: int) -> int:
    """This is a recursive function
    to find the factorial of an integer"""
    if x == 1:
        return 1
    else:
        num = (x * factorial(x-1))
        return num
num = 3
print(f'The factorial of {num} is {factorial(num)}.')

'''
factorial(3)          # 1st call with 3
3 * factorial(2)      # 2nd call with 2
3 * 2 * factorial(1)  # 3rd call with 1
3 * 2 * 1             # return from 3rd call as number=1
3 * 2                 # return from 2nd call
6                     # return from 1st call
'''