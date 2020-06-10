start = input()

num1 = int(start)
num2 = 0
count = 0

num2 = num1//10 + num1%10
num1 = int(str(num1%10) + str(num2%10))
count += 1

while num1 != int(start):
        num2 = num1//10 + num1%10
        num1 = int(str(num1%10) + str(num2%10))
        count += 1

print(count)