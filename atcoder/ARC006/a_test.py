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

    def test_入力例_1(self):
        input = """1 2 3 4 5 6
7
1 2 3 4 5 6"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0 1 3 5 7 9
4
0 2 4 6 8 9"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """0 2 6 7 8 9
4
0 5 6 7 8 9"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1 3 5 6 7 8
9
3 5 6 7 8 9"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """0 1 3 4 5 7
8
2 3 5 7 8 9"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
