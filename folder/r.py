import sys


def fib(n: int)->int:
    n = int(n)
    if n == 0:
        return 0
    if n in(1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(sys.argv[1]))



