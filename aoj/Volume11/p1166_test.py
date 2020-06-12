from p1166 import resolve
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
        input = """2 3
 1
0 1
 0
1 0
 1
9 4
 1 0 1 0 0 0 0 0
0 1 1 0 1 1 0 0 0
 1 0 1 1 0 0 0 0
0 0 0 0 0 0 0 1 1
 0 0 0 1 0 0 1 1
0 0 0 0 1 1 0 0 0
 0 0 0 0 0 0 1 0
12 5
 1 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0 0 0 0
 1 0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 1 0 0 0 0
 0 0 1 0 0 1 0 1 0 0 0
0 0 0 1 1 0 1 1 0 1 1 0
 0 0 0 0 0 1 0 0 1 0 0
0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 1 0 0
0 0"""
        output = """4
0
20"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()