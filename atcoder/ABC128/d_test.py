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
        input = """6 4
-10 8 2 1 2 6"""
        output = """14"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 4
-6 -100 50 -2 -5 -3"""
        output = """44"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6 3
-6 -100 50 -2 -5 -3"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
