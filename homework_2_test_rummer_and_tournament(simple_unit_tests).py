import runner_and_tournament
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = runner_and_tournament.Runner('Усэйн', 10)
        self.runner2 = runner_and_tournament.Runner('Андрей', 9)
        self.runner3 = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            show_result = {}
            for place, runner in result.items():
                show_result[place] = runner.name
            print(show_result)

    def test_1(self):
        tournament = runner_and_tournament.Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        TournamentTest.all_results['test_1'] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_2(self):
        tournament = runner_and_tournament.Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        TournamentTest.all_results['test_2'] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_3(self):
        tournament = runner_and_tournament.Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        TournamentTest.all_results['test_3'] = results
        self.assertTrue(results[max(results.keys())] == "Ник")


if __name__ == '__main__':
    unittest.main()
