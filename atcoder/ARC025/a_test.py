from a import resolve
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

    def test_入力例1(self):
        input = """4 2 0 5 6 2 5
6 1 4 3 6 4 6"""
        output = """33"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """1 2 3 4 5 6 7
2 3 4 5 6 7 8"""
        output = """35"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """0 0 0 0 0 0 0
0 0 0 0 0 0 0"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """8 3 0 2 5 25 252
252 252 2 5 2 5 2"""
        output = """793"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
