arr = []
result = [0,0,0,0,0,0,0,0,0,0]

num1 = int(input())
num2 = int(input())
num3 = int(input())

arr = list(map(int, str(num1*num2*num3)))

for i in arr:
    result[i] += 1

for i in result:
    print(i)