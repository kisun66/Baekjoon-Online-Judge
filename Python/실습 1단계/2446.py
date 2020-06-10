num = int(input())

for i in range(num):
    print(("-"*i)+("*"*((num*2)-(i*2)-1)))

for i in range(num-2, -1, -1):
    print(("-"*i)+("*"*((num*2)-(i*2)-1)))
