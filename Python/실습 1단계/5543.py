burger = []
drink = []
set_menu = []

for i in range(3):
    burger.append(int(input()))

for i in range(2):
    drink.append(int(input()))

for i in burger:
    for j in drink:
        set_menu.append(i + j - 50)

print(min(set_menu))