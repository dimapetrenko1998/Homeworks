from pprint import pprint


file_name = 'text.txt'
with open(file_name, "r") as file:
    file_content = file.read()
    print(file_content)
