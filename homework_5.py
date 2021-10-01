print('Ведите две буквы русского алфавита:')
char1 = input('char1 = ')
char2 = input('char2 = ')

pos_char1 = ord(char1) - 1071
pos_char2 = ord(char2) - 1071
distance = abs(pos_char1 - pos_char2) - 1
if distance == 1:
    distance = '1 буква'
elif 2 <= distance <= 4:
    distance = f'{distance} буквы'
else:
    distance = f'{distance} букв'
print(f'Буква "{char1}" {pos_char1}-я в алфавите\n'
      f'Буква "{char2}" {pos_char2}-я в алфавите\n'
      f'Между буквами {distance}')