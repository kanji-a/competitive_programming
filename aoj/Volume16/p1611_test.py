from p1611 import resolve
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
        input = """4
1 2 3 4
4
1 2 3 1
5
5 1 2 3 6
14
8 7 1 4 3 5 4 1 6 8 10 4 6 5
5
1 3 5 1 3
0"""
        output = """4
4
2
12
0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()