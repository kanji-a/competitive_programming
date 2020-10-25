from c import resolve
import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """3 4
#.##
..#.
#..."""
        output = """1333
2433
1211"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 12
#.##..#...##
#..#..##...#
##.#....##.#
.#..###...#.
#..#..#...##
###...#..###
.###.#######
.#..#....###
.#.##..####.
.###....#..#"""
        output = """233322331133
455432343354
444344443343
444344332454
454335431465
466434554686
466434445796
346554457885
346542135664
235431134432"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
