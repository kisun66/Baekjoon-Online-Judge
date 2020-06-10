num = int(input())

for i in range(num):
    arr = list(map(int, input().split()))
    students = arr[0]
    student_score = arr[1:]

    if students == len(student_score):
        avg = sum(student_score) / students
        count = 0
        
        for j in student_score:
            if j > avg:
                count += 1
            else:
                continue
        
        print("{:.3f}%".format(count/students*100))