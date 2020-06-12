from p1193 import resolve
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
        input = """1
6 9 9 9 9
5
5 9 5 5 9
5 5 6 9 9
4 6 3 6 9
3 3 2 9 9
2 2 1 1 1
10
3 5 6 5 6
2 2 2 8 3
6 2 5 9 2
7 7 7 6 1
4 6 6 4 9
8 9 1 1 8
5 6 1 8 1
6 8 2 1 2
9 6 3 3 5
5 3 8 8 8
5
1 2 3 4 5
6 7 8 9 1
2 3 4 5 6
7 8 9 1 2
3 4 5 6 7
3
2 2 8 7 4
6 5 7 7 7
8 8 9 9 9
0"""
        output = """36
38
99
0
72"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """10
7 5 3 5 4
8 6 5 9 5
5 3 9 7 7
3 3 7 9 8
5 3 2 1 9
8 2 5 2 6
9 1 8 3 8
7 4 7 5 7
4 8 9 7 7
7 7 7 3 3
0"""

        output = """84"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()