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
        input = """9 0 0 18 0 0
9 0 1 18 0 0
12 14 52 12 15 30"""
        output = """9 0 0
8 59 59
0 0 38"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()