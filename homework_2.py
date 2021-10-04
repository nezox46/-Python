number = input('Введите число: ')
odd = 0
even = 0
for f in number:
    i = int(f)
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"У чилса {number} четных цифр - {even}, нечетных цифр - {odd}")
