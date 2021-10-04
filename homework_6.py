from random import randint


def random_number():
    value = randint(0, 101)
    return value


secret_num = random_number()

i = 10

while i <= 10:
    print(f'У вас есть {i} попыток, чтобы угадать число')
    user_number = int(input('Введите число от 0 до 100: '))
    if user_number == secret_num:
        print('Поздравляю, вы отгадали число')
        break
    elif user_number > secret_num:
        print('Вы ввели слишком большее число')
    else:
        print('Вы ввели слишком мальенкое число')
    i -= 1
if i > 10:
    print(f'Вы не отгадали, загаданное число - {secret_num}')
