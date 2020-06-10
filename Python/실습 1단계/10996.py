num = int(input())

if num == 1:
    print("*")
else:
    for i in range(num*2):
        for j in range(1, num+1):
            if i % 2 == 1:
                if j % 2 == 1:
                    print(" ", end="")
                else:
                    print("*", end="")
            else:
                if j % 2 == 1:
                    print("*", end="")
                else:
                    print(" ", end="")
        print("")