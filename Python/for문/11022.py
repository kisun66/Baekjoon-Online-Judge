import sys

t = int(sys.stdin.readline())

for i in range(t):
    num1, num2 = map(int, sys.stdin.readline().split())
    print(f"Case #{i+1}: {num1} + {num2} = {num1+num2}")