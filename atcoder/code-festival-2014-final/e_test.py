from e import resolve
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
        input = """4
1 2 5 1"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """5
1 2 3 4 5"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """3
0 1 0"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """2
0 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例6(self):
        input = """5
0 1 0 -1 0"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例7(self):
        input = """5
0 1 1 0 1"""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
