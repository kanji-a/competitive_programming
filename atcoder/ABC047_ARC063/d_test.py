from d import resolve
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
        input = """3 2
100 50 200"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 8
50 30 40 10 20"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 100
7 10 4 5 9 3 6 8 2 1"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
