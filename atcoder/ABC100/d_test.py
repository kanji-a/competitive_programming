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
        input = """5 3
3 1 4
1 5 9
2 6 5
3 5 8
9 7 9"""
        output = """56"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 3
1 -2 3
-4 5 -6
7 -8 -9
-10 11 -12
13 -14 15"""
        output = """54"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 5
10 -80 21
23 8 38
-94 28 11
-26 -2 18
-69 72 79
-26 -86 -54
-72 -50 59
21 65 -32
40 -94 87
-62 18 82"""
        output = """638"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """3 2
2000000000 -9000000000 4000000000
7000000000 -5000000000 3000000000
6000000000 -1000000000 8000000000"""
        output = """30000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
