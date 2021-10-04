n = int(input())
z = 1
x = 0
for i in range(n):
    x += z
    z /= -2
print(x)
