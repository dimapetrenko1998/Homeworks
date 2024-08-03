import matplotlib.pyplot as plt

# Простой линейный график
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 12, 9]
plt.plot(x, y)
plt.xlabel('X-ось')
plt.ylabel('Y-ось')
plt.title('Пример линейного графика')
plt.show()

import numpy as np

# Создаем массив чисел
array = np.array([1, 2, 3, 4, 5])
print("Созданный массив:")
print(array)
# Возводим каждый элемент массива в квадрат
squared_array = array ** 2
print("\nКвадраты элементов массива:")
print(squared_array)
# Суммируем элементы массива
sum_of_array = np.sum(array)
print("\nСумма элементов массива:")
print(sum_of_array)
