from e import resolve
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
        input = """13 21 1 1
1000 6000
7
1 2
3 7
2 4
5 8
8 9
2 5
3 4
4 7
9 10
10 11
5 9
7 12
3 6
4 5
1 3
11 12
6 7
8 11
6 13
7 8
12 13"""
        output = """11000"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """21 26 2 2
1000 2000
5
16
1 2
1 3
1 10
2 5
3 4
4 6
5 8
6 7
7 9
8 10
9 10
9 11
11 13
12 13
12 15
13 14
13 16
14 17
15 16
15 18
16 17
16 19
17 20
18 19
19 20
19 21"""
        output = """15000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()