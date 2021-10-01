num1, num2, num3 = [x for x in input('Введите три числа, через пробел: ').split()]

if num2 < num1 < num3 or num3 < num1 < num2:
    print(f'Среднее: {num1}')
elif num1 < num2 < num3 or num3 < num2 < num1:
    print(f'Среднее: {num2}')
else:
    print(f'Среднее: {num3}')
