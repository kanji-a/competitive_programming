from ALDS1_6_B import resolve
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
        input = """12
13 19 9 5 12 8 7 4 21 2 6 11"""
        output = """9 5 8 7 4 2 6 [11] 21 13 19 12"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()