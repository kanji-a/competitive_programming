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
        input = """2 5
5 3 2 4 8"""
        output = """1
2
-1
2
1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 10
13 16 6 15 10 18 13 17 11 3"""
        output = """1
1
2
2
3
1
3
2
4
5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 30
35 23 43 33 38 25 22 39 22 6 41 1 15 41 3 20 50 17 25 14 1 22 5 10 34 38 1 12 15 1"""
        output = """1
2
1
2
2
3
4
2
5
6
2
7
6
3
7
6
1
7
4
8
9
6
9
9
4
4
10
9
8
-1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
