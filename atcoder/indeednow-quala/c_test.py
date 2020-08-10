from c import resolve
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

    def test_入力例1(self):
        input = """15
0
0
0
1
1
2
3
4
5
6
6
6
8
9
10
3
0
4
12"""
        output = """11
7
0"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """9
3
3
3
2
2
2
1
1
1
1
4"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """4
0
0
0
0
1
0"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
