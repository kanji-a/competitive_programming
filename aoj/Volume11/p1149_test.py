from p1149 import resolve
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
        input = """3 5 6
1 18
2 19
1 2
3 4 1
1 1
2 1
3 1
0 2 5
0 0 0"""
        output = """4 4 6 16
1 1 1 1
10"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()