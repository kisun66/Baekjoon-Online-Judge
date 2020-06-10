num = int(input())

for i in range(num):
    score = 0
    bonus_score = 0
    ox = list(input())
    for j in range(len(ox)):
        if ox[j] == "O":
            if ox[j - 1] == "O" and j != 0:
                bonus_score += 1
            score = score + 1 + bonus_score
        else:
            bonus_score = 0
    print(score)