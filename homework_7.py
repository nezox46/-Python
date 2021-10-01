a, b, c = [float(x) for x in input('Введите три числа, через пробел: ').split()]

if b < c or c < b or c < a:
    print('Это не треугольник')
else:
    if a == b or b == c or c == a:
        if a == b and a == c:
            print('Треугольник равносторонний')
        else:
            print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')