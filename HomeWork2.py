# Задача 2
print('Введите координаты x, y, z ')
x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))
if not(x or y or z) == (not x) and (not y) and (not z):
    print(f'Истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат - ' ,True)
else:
    print(f'Истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат - ' , False)
    