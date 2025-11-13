import unittest
from film import Film

class TestFilm(unittest.TestCase):

    def test_est_classique(self):
        f1 = Film("Old Movie", "Realisateur", 1980, 7.5)
        self.assertTrue(f1.est_classique())
        f2 = Film("New Movie", "Realisateur", 2005, 8.0)
        self.assertFalse(f2.est_classique())

    def test_to_json_and_from_json(self):
        f = Film("Test", "Director", 1995, 9.0)
        json_str = f.to_json()
        f2 = Film.from_json(json_str)
        self.assertEqual(f, f2)

    def test_sort_by_note(self):
        f1 = Film("A", "R", 2000, 7.0)
        f2 = Film("B", "R", 2000, 9.0)
        films = [f2, f1]
        films_sorted = sorted(films, key=lambda f: f.note)
        self.assertEqual(films_sorted, [f1, f2])

if __name__ == "__main__":
    unittest.main()
