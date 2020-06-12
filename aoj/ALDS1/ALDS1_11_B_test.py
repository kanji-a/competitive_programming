from ALDS1_11_B_stack import resolve
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
        input = """4
1 1 2
2 1 4
3 0
4 1 3"""
        output = """1 1 8
2 2 7
3 4 5
4 3 6"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """6
1 2 2 3
2 2 3 4
3 1 5
4 1 6
5 1 6
6 0"""
        output = """1 1 12
2 2 11
3 3 8
4 9 10
5 4 7
6 5 6"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """6
1 2 2 4
2 1 5
3 2 5 6
4 0
5 1 4
6 1 6"""
        output = """1 1 8
2 2 7
3 9 12
4 4 5
5 3 6
6 10 11"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """3
1 1 2
2 1 3
3 1 1"""
        output = """1 1 6
2 2 5
3 3 4"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()