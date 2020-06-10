n = int(input())
temp = 1

for i in reversed(range(n)):
    print(" " * i, end="")
    print("*" * temp)
    temp += 1