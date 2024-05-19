#Первое задание

str_ = '2' * 50
print(str_)
repl = str_.replace('2', '*')
print(repl)

#Второе задние

user_list = input("Введите пользователей и номер телефона через пробел: ").split()
user_dict = {}

for i in range(0, len(user_list), 2):
    name = user_list[i]
    phone_number = user_list[i+1]
    user_dict[name] = phone_number

print("Словарь пользователей:", user_dict)

#Третье задание

input_str1 = input('Введите число состоящее из чисел 8,6,3: ')
print(int(input_str1))
repl1 = input_str1.replace('8', '*').replace('6', '^').replace('3', '№')
print(repl1)
input_str2 = input('Введите слово: ').upper()
print(input_str2)

#Четвертое задание

dictionary = {'слово1': 'перевод1', 'слово2': 'перевод2', 'слово3': 'перевод3', 'слово4': 'перевод4', 'слово5': 'перевод5'}

word1 = input("Введите слово из словаря: ")

word2 = input("Введите новое значение для слова: ")

print("Изначальный перевод слова", word1, ":", dictionary[word1])

dictionary[word1] = word2

print("Словарь после замены значения:", dictionary)

#Пятое задание

new_str1 = 'мккопрллтоктдаиеккцааа'
new_str2 = 'будешь сыт'

enumeration = new_str2[:7:-1]

enumeration2 = new_str1[:20:3]
print(enumeration + ' ' + enumeration2)
