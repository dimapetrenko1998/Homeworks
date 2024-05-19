immutable_var = ("String", 1, True)
print(immutable_var)
#immutable_var[0] = 200
#print(immutable_var) В Python нельзя изменить значения элементов кортежа,
# так как кортежи являются неизменяемыми (immutable) структурами данных.
# Это означает, что после создания кортежа, его элементы не могут быть изменены,
# добавлены или удалены. Если попытаться изменить значение элемента кортежа, будет возбуждено исключение типа TypeError.
mutable_list = ['String', 1, True]
mutable_list[0] = 2
print(mutable_list)