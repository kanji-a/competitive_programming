from e import resolve
import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    maxDiff = None
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """3 1
5 3 2
1 4 8
7 6 9"""
        output = """19
X..
..X
.X."""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 2
10 10 1
10 10 1
1 1 10"""
        output = """50
XX.
XX.
..X"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
