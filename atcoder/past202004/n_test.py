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
        input = """2 4
1 3 6 10
3 6 6 20
4 7
-1 -1
1 4
7 13"""
        output = """30
0
10
0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 3
-3 5 4 100
1 9 7 30
1 9
1 8
8 10"""
        output = """130
100
30"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 10
17 2 17 1000000000
7 12 12 1000000000
2 12 8 1000000000
2 12 2 1000000000
3 9 16 1000000000
8 13 15 1000000000
8 1 3 1000000000
15 9 17 1000000000
16 5 5 1000000000
13 12 9 1000000000
17 3
4 10
1 9
5 3
17 12
14 19
19 17
17 11
16 17
12 16"""
        output = """1000000000
1000000000
0
0
5000000000
4000000000
6000000000
3000000000
5000000000
3000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
