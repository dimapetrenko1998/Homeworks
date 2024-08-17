from runner import Runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner("Тестовый бегун")  # Создаем объект класса Runner с произвольным именем
        for _ in range(10):  # Вызываем метод walk 10 раз
            runner.walk()
        self.assertEqual(runner.distance, 50)  # Проверяем, что расстояние равно 50

    def test_run(self):
        runner = Runner("Тестовый бегун 2")  # Создаем объект класса Runner с произвольным именем
        for _ in range(10):  # Вызываем метод run 10 раз
            runner.run()
        self.assertEqual(runner.distance, 100)  # Проверяем, что расстояние равно 100

    def test_challenge(self):
        runner1 = Runner("Бегун 1")  # Создаем первого бегуна
        runner2 = Runner("Бегун 2")  # Создаем второго бегуна

        for _ in range(10):  # Вызываем методы run и walk 10 раз
            runner1.run()
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance)  # Проверяем, что расстояния не равны


if __name__ == '__main__':
    unittest.main()
