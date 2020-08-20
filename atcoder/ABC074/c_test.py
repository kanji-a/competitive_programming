from c import resolve
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
        input = """1 2 10 20 15 200"""
        output = """110 10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 2 1 2 100 1000"""
        output = """200 100"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """17 19 22 26 55 2802"""
        output = """2634 934"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1 2 10 20 1 200"""
        output = """100 0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
