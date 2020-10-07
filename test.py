import sys

def rec(n):
    if n==0:
        return 0
    rec(n-1)


print(sys.getrecursionlimit())
sys.setrecursionlimit(2**30)
print(sys.getrecursionlimit())
rec(1000000)
print("done")