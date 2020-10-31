from p import resolve
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
        input = """3
1 2
2 3"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 2
1 3
1 4"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10
8 5
10 8
6 5
1 5
4 8
2 10
3 6
9 2
1 7"""
        output = """157"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
