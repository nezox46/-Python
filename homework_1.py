num = int(input('Введите трехзначное число: '))
a = num // 100
b = (num % 100) // 10
c = num % 10
multiply = a * b * c
summation = a + b + c
print (f'произведение цифр для числа {num} - {multiply}\nсложение цифр для числа {num} - {summation}')