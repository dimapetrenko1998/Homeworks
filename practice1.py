class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
    Класс пользоывателя, содержащий атрибуты: логин, пароль
    """
    def __init__(self, username, password, passwork_confirm):
        self.username = username
        if password == passwork_confirm:
            self.password = password


if __name__ == '__main__':
    database = Database()
    user = User(input('Введите логин: '), input('Введите пароль: '), input('Повторите пароль: '))
    database.add_user(user.username, user.password)