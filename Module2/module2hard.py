numbers = int(input('Введите число от 3 до 20:'))
result = ''

for i in range(1, numbers):
    for j in range(i + 1, numbers + 1):
        if numbers % (i + j) == 0:
            if str(i) + str(j) not in result and str(j) + str(i) not in result:
                result += str(i) + str(j)
print(result)
