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
        input = """4 5 8
1 1
1 4
1 5
2 3
3 1
3 2
3 4
4 4"""
        output = """0
0
0
2
4
0
0
0
0
0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 10 20
1 1
1 4
1 9
2 5
3 10
4 2
4 7
5 9
6 4
6 6
6 7
7 1
7 3
7 7
8 1
8 5
8 10
9 2
10 4
10 9"""
        output = """4
26
22
10
2
0
0
0
0
0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000000000 1000000000 0"""
        output = """999999996000000004
0
0
0
0
0
0
0
0
0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
