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
        input = """3
2 2 4"""
        output = """4 0 4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
3 8 7 5 5"""
        output = """2 4 12 2 8"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
1000000000 1000000000 0"""
        output = """0 2000000000 0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
