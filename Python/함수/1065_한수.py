num = int(input())

def han(num):
    result = 0

    for i in range(1, num+1):
        if 0 < i < 100:
            result += 1
        else:
            arr = list(map(int, str(i)))
            arr_temp = []

            for j in range(len(arr)-1):
                temp = arr[j] - arr[j+1]
                arr_temp.append(temp)
            
            if len(set(arr_temp)) == 1:
                result+=1
            else:
                continue

    return result

print(han(num))