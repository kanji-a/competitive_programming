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
        input = """3 3
20 21 22
30 22 15"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """3 4
10 11 10
12 10 11 25"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """5 5
10 10 10 10 10
10 10 10 10 10"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """5 5
10 11 12 13 14
30 31 32 33 34"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
