from NTL_1_A import resolve
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
        input = """12"""
        output = """12: 2 2 3"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """126"""
        output = """126: 2 3 3 7"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()