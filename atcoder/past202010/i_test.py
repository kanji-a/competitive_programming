from i import resolve
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
        input = """4
10 20 40 30"""
        output = """20"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """20
13 76 46 15 50 98 93 77 31 43 84 90 6 24 14 37 73 29 43 9"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
