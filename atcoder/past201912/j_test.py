from j import resolve
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
        input = """5 6
9 9 9 9 1 0
9 9 9 9 1 9
9 9 9 1 1 1
9 1 1 1 9 1
0 1 9 9 9 0"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 10
1 2 265 1544 0 1548 4334 9846 58 0
21 0 50 44 2 388 5 0 0 4
170 0 2 1 54 1379 50 3 41 0
310 0 1 0 2163 0 226 26 3 12
151 33 0 9 0 0 0 36 365 2286
0 3 12 3 9 317 645 100 21 4
52 1 569 0 144 0 6 202 25 0
8869 19 2058 1948 1252 1002 7 1750 0 5
0 3 8 29 2 4403 0 0 0 5
0 17 93 9367 159 6 1 216 0 0"""
        output = """246"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
