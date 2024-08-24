import unittest
from runner_2 import Runner, Tournament


# Декоратор для пропуска тестов
def skip_if_frozen(test_func):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            print("Тесты в этом кейсе заморожены")
            raise unittest.SkipTest("Тесты в этом кейсе заморожены")
        return test_func(self, *args, **kwargs)

    return wrapper


# Обновляем классы тестов
class Runner(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_challenge(self):
        # Ваш тест
        pass

    @skip_if_frozen
    def test_run(self):
        # Ваш тест
        pass

    @skip_if_frozen
    def test_walk(self):
        # Ваш тест
        pass


class Tournament(unittest.TestCase):
    is_frozen = True

    @skip_if_frozen
    def test_first_tournament(self):
        # Ваш тест
        pass

    @skip_if_frozen
    def test_second_tournament(self):
        # Ваш тест
        pass

    @skip_if_frozen
    def test_third_tournament(self):
        # Ваш тест
        pass


# Создание TestSuite
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Runner))
    suite.addTest(unittest.makeSuite(Tournament))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
