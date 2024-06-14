class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password  # Хэшированный пароль (например, md5)
        self.age = age


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []  # Список объектов User
        self.videos = []  # Список объектов Video
        self.current_user = None  # Текущий пользователь

    def log_in(self, login, password):
        # Поиск пользователя по логину и паролю
        for user in self.users:
            if user.nickname == login and user.password == password:
                self.current_user = user
                return True
        return False

    def register(self, nickname, password, age):
        # Добавление пользователя, если его нет
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        # Добавление видео в список
        for video in videos:
            if video.title not in [v.title for v in self.videos]:
                self.videos.append(video)

    def get_videos(self, search_word):
        # Поиск видео по ключевому слову (без учета регистра)
        return [video.title for video in self.videos if search_word.lower() in video.title.lower()]

    def watch_video(self, video_title):
        # Воспроизведение видео и отчет о времени
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for video in self.videos:
            if video.title.lower() == video_title.lower():
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста, покиньте страницу")
                    return
                while video.time_now < video.duration:
                    print(f"Секунда воспроизведения: {video.time_now}")
                    video.time_now += 1
                    # Здесь можно добавить паузу между выводами секунд
                print("Конец видео")
                video.time_now = 0
                return
        print(f"Видео '{video_title}' не найдено")


if __name__ == "__main__":
    urtube = UrTube()
    urtube.register("user1", "password123", 25)
    urtube.add(Video("Python Basics", 120))
    urtube.log_in("user1", "password123")
    urtube.watch_video("Python Basics")
    urtube.log_out()