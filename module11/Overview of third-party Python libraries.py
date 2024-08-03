import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 12, 9]
plt.plot(x, y)
plt.xlabel('X-ось')
plt.ylabel('Y-ось')
plt.title('Пример линейного графика')
plt.show()

import numpy as np

array = np.array([1, 2, 3, 4, 5])
print("Созданный массив:")
print(array)

squared_array = array ** 2
print("\nКвадраты элементов массива:")
print(squared_array)

sum_of_array = np.sum(array)
print("\nСумма элементов массива:")
print(sum_of_array)

'''Библиотека NumPy предоставляет мощные инструменты для работы с многомерными массивами и матрицами. Она позволяет 
выполнять различные математические операции, такие как сложение, умножение и возведение в степень, с высокой 
производительностью. Благодаря NumPy я могу легко обрабатывать большие объемы числовых данных, что делает его 
незаменимым инструментом для научных исследований и анализа данных. Например, функции для линейной алгебры и 
статистики позволяют быстро выполнять сложные вычисления, что значительно ускоряет процесс анализа. Matplotlib 
является одной из самых популярных библиотек для визуализации данных в Python. Она позволяет создавать разнообразные 
графики, такие как линейные графики, гистограммы, диаграммы рассеяния и многие другие. С помощью Matplotlib я могу 
наглядно представлять результаты своих вычислений и анализов, что помогает лучше понять данные и выявить 
закономерности. Например, возможность настраивать внешний вид графиков, добавлять аннотации и изменять масштабы 
делает визуализацию более информативной и привлекательной.С помощью NumPy и Matplotlib я значительно расширил 
функциональность Python для работы с данными. Эти библиотеки позволяют не только выполнять сложные математические 
операции, но и визуализировать результаты, что делает Python мощным инструментом для анализа данных. Я могу легко 
интегрировать эти библиотеки в свои проекты, что позволяет мне более эффективно решать задачи в области науки и 
анализа данных. В целом, использование NumPy и Matplotlib сделало мой опыт работы с Python более продуктивным и 
увлекательным, открыв новые горизонты для анализа и визуализации данных.'''