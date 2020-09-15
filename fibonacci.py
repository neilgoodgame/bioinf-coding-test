"""
Construct a function that returns the Nth value of the fibonacci sequence.
Any invalid input should return None.

e.g.
    Fn = Fn-1 + Fn-2
with seed values
   F0 = 0 and F1 = 1.
"""

def fibonacci(N):
    pass





#
#  Tests
#
import test.fibonacci_reference as fr

def test(N):
    user = fibonacci(N)
    ref = fr.fibonacci(N)
    if user != ref:
        raise AssertionError('N={}: expecting {}, got {}'.format(N, ref, user))

if __name__ == '__main__':
    test(-1)
    test(0)
    test(1)
    test(2)
    test(3)
    test(5)
    test(10)
    test(1000)

