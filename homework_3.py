x1, y1, x2, y2 = [
    int(x) for x in input('Введите кординаты (x1 y1 x2 y2): ').split()
]
k = (y2 - y1)/(x2 - x1)
b = y1 - k * x1
round(k)
round(b)

print(f'Уравнение прямой: y = {k:.0f}x + {b:.0f2}')