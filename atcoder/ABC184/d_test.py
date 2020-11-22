from d import resolve
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
        input = """99 99 99"""
        output = """1.000000000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """98 99 99"""
        output = """1.331081081"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """0 0 1"""
        output = """99.000000000"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """31 41 59"""
        output = """91.835008202"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
