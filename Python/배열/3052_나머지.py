num = []

for i in range(10):
    num.append(int(input()))

for i in range(10):
    num[i] = num[i] % 42

print(len(set(num)))