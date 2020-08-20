from b import resolve
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
        input = """6
2 1
2 2
3 2
5 3
2 2
3 3"""
        output = """2 3 0
0 4 1
4 1 0
5 0 0
0 4 1
3 2 0"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """2
1999 3
2000 1"""
        output = """0 1 0
1 0 0"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """8
3200 2
2800 3
2800 2
2700 1
2800 2
3200 1
2700 1
3200 3"""
        output = """6 1 0
2 5 0
3 3 1
0 6 1
3 3 1
6 1 0
0 6 1
6 1 0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
