num = int(input('Введите номер буквы в алфавите от 1 до 26: '))
if num <= 26:
    num = chr(num + 64)
    print(f'Это буква "{num}"')
else:
    print('Вы ввели недоступное значение')
