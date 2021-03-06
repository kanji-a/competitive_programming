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
        input = """4
4 3 2 1"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """4
1 2 3 5"""
        output = """1.333"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """4
1000000000 1000000000 1000000000 1000000000"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """4
1000000000 324219581 581395481 2319"""
        output = """-333332560.333333313"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
