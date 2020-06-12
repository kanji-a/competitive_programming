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
    def test_入力例_1(self):
        input = """3 5
4 2 1
2 3 1"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3 8
4 2 1
2 3 1"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """11 14
3 1 4 1 5 9 2 6 5 3 5
8 9 7 9 3 2 3 8 4 6 2"""
        output = """12"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()