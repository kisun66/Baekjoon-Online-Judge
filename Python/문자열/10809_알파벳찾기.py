#97~122 = a~z
temp = input()
word = [chr(i) for i in range(97, 123)]

for i in range(len(word)):
    num = temp.find(word[i])
    word[i] = num

print(" ".join(map(str, word)))