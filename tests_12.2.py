import unittest
import runner_and_tournament


class TournamentTest(unittest.TestCase):
    all_results = None

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        res = {}
        for key, value in cls.all_results.items():
            for k, v in value.items():
                res[k] = str(v)
            print(res)

    def setUp(self):
        self.usain = runner_and_tournament.Runner('Усэйн', 10)
        self.andrew = runner_and_tournament.Runner('Андрей', 9)
        self.nick = runner_and_tournament.Runner('Ник', 3)

    def test_run_first(self):
        first_run = runner_and_tournament.Tournament(90, self.usain, self.nick)
        result = first_run.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[result.values()] = result

    def test_run_second(self):
        second_run = runner_and_tournament.Tournament(90, self.andrew, self.nick)
        result = second_run.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[result.values()] = result

    def test_run_third(self):
        third_run = runner_and_tournament.Tournament(90, self.andrew, self.usain, self.nick)
        result = third_run.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[result.values()] = result


if __name__ == '__main__':
    unittest.main()