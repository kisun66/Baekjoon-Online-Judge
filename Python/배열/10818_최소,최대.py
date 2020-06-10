num = int(input())
num2 = list(map(int, input().split()))

if num == len(num2):
    print(f"{min(num2)} {max(num2)}")