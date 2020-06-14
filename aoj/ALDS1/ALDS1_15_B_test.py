from ALDS1_15_B import resolve
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
        input = """3 50
60 10
100 20
120 30"""
        output = """240"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3 50
60 13
100 23
120 33"""
        output = """210.90909091"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()