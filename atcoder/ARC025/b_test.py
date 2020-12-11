from b import resolve
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
        input = """3 4
4 6 2 5
3 5 6 7
2 5 5 6"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """2 2
4 0
7 3"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """2 3
0 0 0
1 2 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """3 3
1 2 3
6 5 4
7 8 9"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例5(self):
        input = """1 5
0 1 2 3 4"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
