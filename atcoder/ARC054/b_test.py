from b import resolve
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
        input = """3.0000"""
        output = """2.8708930019"""
        self.assertIO(input, output)
    def test_入力例2(self):
        input = """0.0400"""
        output = """0.0400000000"""
        self.assertIO(input, output)
    def test_入力例3(self):
        input = """1000000000000000000.0000"""
        output = """90.1855078128"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()