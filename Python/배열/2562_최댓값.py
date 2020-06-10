num = []
max_num = 0

for i in range(9):
    num.append(int(input()))

max_num = max(num)

for i in range(9):
    if max_num == num[i]:
        print(max_num)
        print(i+1)
        break
    else:
        continue