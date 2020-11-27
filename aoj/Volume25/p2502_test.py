from p2502_naive import resolve
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
4 5 15
2 3 4
7 8 39
2
6
8"""
        output = """19
39"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1
2 3 10
2
3
1"""
        output = """-1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()