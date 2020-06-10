num1 = int(input())
num2 = list(map(int, list(input())))

if num1 == len(num2):
    print(sum(num2))