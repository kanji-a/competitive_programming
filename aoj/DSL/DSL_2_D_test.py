from DSL_2_D import resolve
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
        input = """3 5
0 0 1 1
0 1 2 3
0 2 2 2
1 0
1 1"""
        output = """1
3"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """1 3
1 0
0 0 0 5
1 0"""
        output = """2147483647
5"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """8 10
0 1 6 5
0 2 7 2
0 2 5 7
1 3
0 4 6 6
1 0
0 0 7 9
1 2
1 3
0 1 7 2"""
        output = """7
2147483647
9
9"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()