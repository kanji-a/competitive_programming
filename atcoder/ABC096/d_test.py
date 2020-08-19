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
        input = """5"""
        output = """3 5 7 11 31"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6"""
        output = """2 3 5 7 11 13"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8"""
        output = """2 5 7 13 19 37 67 79"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
