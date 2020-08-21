from c import resolve
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
        input = """1 25 25 50"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 50 50 0"""
        output = """312500008"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 100 0 0"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """100000 31 41 28"""
        output = """104136146"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
