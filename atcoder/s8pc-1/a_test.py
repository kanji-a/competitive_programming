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
    def test_入力例1(self):
        input = """9"""
        output = """135.000000000000"""
        self.assertIO(input, output)
    def test_入力例2(self):
        input = """1001"""
        output = """1.080000000000"""
        self.assertIO(input, output)
    def test_入力例3(self):
        input = """114514"""
        output = """0.009431243614"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()