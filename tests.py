import sys
import unittest
from boggle_solver import Boggle

# Ensure workspace path is available
sys.path.append("/home/codio/workspace/")


class TestAlgScalabilityCases(unittest.TestCase):
    """Tests for normal and scalability Boggle grids."""

    def test_normal_case_3x3(self):
        grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
        dictionary = ["abc", "abdhi", "abi", "ef", "cfi", "dea"]
        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.get_solution()]
        expected = ["ABC", "ABDHI", "CFI", "DEA"]
        self.assertEqual(sorted(expected), sorted(solution))

    def test_scalability_4x4(self):
        grid = [
            ["A", "B", "C", "D"],
            ["E", "F", "G", "H"],
            ["I", "J", "K", "L"],
            ["M", "N", "O", "P"],
        ]
        dictionary = ["afkp", "bfj", "cfil", "dg", "mnop"]
        mygame = Boggle(grid, dictionary)
        solution = [x.lower() for x in mygame.get_solution()]
        expected = ["afkp", "bfj", "mnop"]
        self.assertEqual(sorted(expected), sorted(solution))


class TestSimpleEdgeCases(unittest.TestCase):
    """Tests for edge and boundary cases."""

    def test_square_grid_1x1(self):
        grid = [["A"]]
        dictionary = ["a", "b", "c"]
        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.get_solution()]
        expected = []  # Solver ignores single letters (min length = 3)
        self.assertEqual(sorted(expected), sorted(solution))

    def test_empty_grid_0x0(self):
        grid = [[]]
        dictionary = ["hello", "there", "general", "kenobi"]
        mygame = Boggle(grid, dictionary)
        self.assertEqual([], mygame.get_solution())

    def test_empty_dictionary(self):
        grid = [["A", "B"], ["C", "D"]]
        dictionary = []
        mygame = Boggle(grid, dictionary)
        self.assertEqual([], mygame.get_solution())

    def test_single_letter_word_match(self):
        grid = [["A", "B"], ["C", "D"]]
        dictionary = ["a"]
        mygame = Boggle(grid, dictionary)
        expected = []
        self.assertEqual(sorted(expected), sorted(mygame.get_solution()))

    def test_invalid_characters(self):
        grid = [["A", "1"], ["B", "C"]]
        dictionary = ["abc"]
        mygame = Boggle(grid, dictionary)
        self.assertEqual([], mygame.get_solution())


class TestCompleteCoverage(unittest.TestCase):
    """Tests for general and complete word coverage."""

    def test_simple_word(self):
        grid = [["C", "A"], ["T", "S"]]
        dictionary = ["cat"]
        mygame = Boggle(grid, dictionary)
        solution = [x.lower() for x in mygame.get_solution()]
        self.assertIn("cat", solution)

    def test_diagonal_word(self):
        grid = [["C", "A"], ["R", "T"]]
        dictionary = ["crt"]
        mygame = Boggle(grid, dictionary)
        solution = [x.lower() for x in mygame.get_solution()]
        self.assertIn("crt", solution)

    def test_long_word_across_board(self):
        grid = [
            ["T", "E", "S", "T"],
            ["A", "B", "C", "D"],
            ["E", "F", "G", "H"],
            ["I", "J", "K", "L"],
        ]
        dictionary = ["test"]
        mygame = Boggle(grid, dictionary)
        solution = [x.lower() for x in mygame.get_solution()]
        self.assertIn("test", solution)


class TestQuAndSt(unittest.TestCase):
    """Tests for special tiles 'Qu' and 'St'."""

    def test_qu_case(self):
        grid = [["Qu", "A"], ["T", "R"]]
        dictionary = ["qua", "quar"]
        mygame = Boggle(grid, dictionary)
        solution = [x.lower() for x in mygame.get_solution()]
        self.assertTrue("qua" in solution or "quar" in solution)

    def test_st_case(self):
        grid = [["St", "A"], ["R", "T"]]
        dictionary = ["star", "start"]
        mygame = Boggle(grid, dictionary)
        solution = [x.lower() for x in mygame.get_solution()]
        self.assertTrue("star" in solution or "start" in solution)


if __name__ == "__main__":
    unittest.main()
