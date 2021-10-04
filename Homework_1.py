def calculator():
    a = int(input('Введите число A: '))
    b = int(input('Введите число B: '))
    operator = input('Введите знак операции (+, -, *, /) или 0 (нижний регистр) для выхода\n')
    operation = ['+', '-', '*', '/']
    if operator == '0':
        quit()
    elif operator not in operation:
        print('Введите знак из списка!')
    elif operator == operation[0]:
        print(f'Результат {a} + {b} = {a + b:.0f}')
        return calculator()
    elif operator == operation[1]:
        print(f'Результат {a} - {b} = {a - b:.0f}')
        return calculator()
    elif operator == operation[2]:
        print(f'Результат {a} * {b} = {a * b:.0f}')
        return calculator()
    elif operator == operation[3]:
        print(f'Результат {a} / {b} = {a / b:.0f}')
        return calculator()
    else:
        pass


calculator()
