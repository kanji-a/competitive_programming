from l import resolve
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
        input = """2
3 1 200 1000
5 20 30 40 50 2
5
1 1 1 2 2"""
        output = """20
30
40
200
1000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
6 8 24 47 29 73 13
1 4
5 72 15 68 49 16
5 65 20 93 64 91
6 100 88 63 50 90 44
2 6 1
10 14 2 76 28 21 78 43 11 97 70
5 31 9 62 84 40
8 10 46 96 23 98 19 38 51
2 37 77
20
1 1 1 1 2 2 2 1 1 2 2 2 2 2 1 2 1 2 2 1"""
        output = """100
88
72
65
93
77
68
63
50
90
64
91
49
46
44
96
37
31
62
20"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1
1 1
1
2"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
