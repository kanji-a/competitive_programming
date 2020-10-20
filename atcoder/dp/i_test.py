from i_inline import resolve
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
0.30 0.60 0.80"""
        output = """0.612"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1
0.50"""
        output = """0.5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
0.42 0.01 0.42 0.99 0.42"""
        output = """0.3821815872"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
