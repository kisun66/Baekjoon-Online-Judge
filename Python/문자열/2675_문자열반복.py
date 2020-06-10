num = int(input())

# 함수
def question(a, b):
    result = ""
    arr = list(b)

    for i in arr:
        
        for j in range(a):
            result += i

    return result

# 결과
for i in range(num):
    a, b = input().split()
    print(question(int(a), b))