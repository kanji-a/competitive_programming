from d import resolve
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
        input = """3
0 1 3
1 0 2
3 2 0"""
        output = """3"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3
0 1 3
1 0 1
3 1 0"""
        output = """-1"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """5
0 21 18 11 28
21 0 13 10 26
18 13 0 23 13
11 10 23 0 17
28 26 13 17 0"""
        output = """82"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """3
0 1000000000 1000000000
1000000000 0 1000000000
1000000000 1000000000 0"""
        output = """3000000000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()