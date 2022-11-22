# Задача 1
number = int(input('Введите цифру дня недели от 1 до 7: '))
if number == 6 or number == 7:
  print(f'{number} - это выходной')
elif number >= 1 and number <= 7:
  print(f'{number} - это точно будний день')
else:
  print(f'{number}  - хмм что то мне подсказывает что то такого дня недели нет. Давай еще раз')
