from runner_2 import Runner, Tournament
import unittest

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runners = [
            Runner("Усэйн", speed=10),
            Runner("Андрей", speed=9),
            Runner("Ник", speed=3)
        ]

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    def test_usain_and_nick(self):
        tournament = Tournament(90, self.runners[0], self.runners[2])  # Усэйн и Ник
        results = tournament.start()
        self.assertTrue(results)
        self.assertEqual(results[max(results.keys())], "Ник")  # Ожидаем, что Ник будет последним
        self.all_results[1] = results

    def test_andrey_and_nick(self):
        tournament = Tournament(90, self.runners[1], self.runners[2])  # Андрей и Ник
        results = tournament.start()
        self.assertTrue(results)
        self.assertEqual(results[max(results.keys())], "Ник")  # Ожидаем, что Ник будет последним
        self.all_results[2] = results

    def test_all_three(self):
        tournament = Tournament(90, *self.runners)  # Все трое
        results = tournament.start()
        self.assertTrue(results)
        self.assertEqual(results[max(results.keys())], "Ник")  # Ожидаем, что Ник будет последним
        self.all_results[3] = results


if __name__ == "__main__":
    unittest.main()
