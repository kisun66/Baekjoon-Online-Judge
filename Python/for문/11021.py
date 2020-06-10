import sys

t = int(sys.stdin.readline())

for i in range(t):
    num1, num2 = map(int, sys.stdin.readline().split())
    print("Case #{}: {}".format(i+1, num1+num2))