"""
Reference implementation of fibonacci sequence generator
Taken from: https://www.geeksforgeeks.org/python-program-for-program-for-fibonacci-numbers-2/

Will exceed max recursion depth n>=10000
"""

FibArray = [0, 1]


def fibonacci(n):
    if n < 0:
        None
    elif n in (0, 1):
        return FibArray[n]
    elif n <= len(FibArray):
        return FibArray[n - 1]
    else:
        temp_fib = fibonacci(n - 1) + fibonacci(n - 2)
        FibArray.append(temp_fib)
        return temp_fib
