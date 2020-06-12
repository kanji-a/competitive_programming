from b import resolve
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
        input = """0 2
6 3
2 4"""
        output = """2.061552812808830"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """0 5
8 6
9 1
2 0
1 0
0 1"""
        output = """0.500000000000000"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """3 0
5 2 3
-1 0 2
2 -6 4"""
        output = """2.000000000000000"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """1 1
0 0 5
6 -3"""
        output = """1.708203932499369"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()