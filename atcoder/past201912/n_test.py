from n import resolve
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
        input = """3 10 5
1 3 100
8 10 123
4 6 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """22 30 10
0 30 1000000000
0 30 1000000000
0 30 1000000000
7 30 261806
6 19 1
5 18 1238738
12 28 84
10 14 5093
9 20 9
15 26 8739840
6 8 240568
14 19 198
2 4 1102
1 29 5953283
9 20 183233
9 13 44580
6 23 787237159
12 14 49
28 29 9020727
14 20 318783
2 19 9862194
9 30 166652"""
        output = """3805189325"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
