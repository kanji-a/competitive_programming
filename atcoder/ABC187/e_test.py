from e import resolve
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
        input = """5
1 2
2 3
2 4
4 5
4
1 1 1
1 4 10
2 1 100
2 2 1000"""
        output = """11
110
1110
110
100"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7
2 1
2 3
4 2
4 5
6 1
3 7
7
2 2 1
1 3 2
2 2 4
1 6 8
1 3 16
2 4 32
2 1 64"""
        output = """72
8
13
26
58
72
5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """11
2 1
1 3
3 4
5 2
1 6
1 7
5 8
3 9
3 10
11 4
10
2 6 688
1 10 856
1 8 680
1 8 182
2 2 452
2 4 183
2 6 518
1 3 612
2 6 339
2 3 206"""
        output = """1657
1657
2109
1703
1474
1657
3202
1474
1247
2109
2559"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
