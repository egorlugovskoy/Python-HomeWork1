# Задача 3
x = int(input('Введите x = '))
y = int(input('Введите y = '))
if x > 0 and y > 0:
    print(f'x = {x}, y = {y} -> это 100% 1 четверть')
elif x < 0 and y > 0:
    print(f'x = {x}, y = {y} -> по любому 2 четверть')
elif x < 0 and y < 0:
    print(f'x = {x}, y = {y} -> сомнений нет это 3 четверть')
elif x > 0 and y < 0:
    print(f'x = {x}, y = {y} -> если все верно считаю, то это 4 четверть')
else:
    x == 0 and y == 0
    print('Ненене никаких нулей. Давай еще раз')