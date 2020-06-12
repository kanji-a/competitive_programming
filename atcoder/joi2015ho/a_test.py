from a import resolve
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
        input = """4 4
1 3 2 4
120 90 100
110 50 80
250 70 130"""
        output = """550"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """8 5
7 5 3 5 4
12 5 8
16 2 1
3 1 5
17 12 17
19 7 5
12 2 19
4 1 3"""
        output = """81"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()