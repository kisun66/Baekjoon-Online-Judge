import sys

n, x = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

if len(a) == n:

    for i in a:

        if i < x:
            print(i, end=" ")