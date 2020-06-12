from p1167 import resolve
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
        input = """40
14
5
165
120
103
106
139
0"""
        output = """2 6
2 14
2 5
1 1
1 18
5 35
4 4
3 37"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()