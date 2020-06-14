from ALDS1_9_B import resolve
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
        input = """10
4 1 3 2 16 9 10 14 8 7"""
        output = """ 16 14 10 8 7 9 3 2 4 1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()