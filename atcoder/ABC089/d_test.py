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
        input = """3 3 2
1 4 3
2 5 7
8 9 6
1
4 8"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 2 3
3 7
1 4
5 2
6 8
2
2 2
2 2"""
        output = """0
0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 5 4
13 25 7 15 17
16 22 20 2 9
14 11 12 1 19
10 6 23 8 18
3 21 5 24 4
3
13 13
2 10
13 13"""
        output = """0
5
0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
