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
        input = """3
abc"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例2(self):
        input = """6
abcabc"""
        output = """-1"""
        self.assertIO(input, output)
    def test_入力例3(self):
        input = """7
atcoder"""
        output = """-1"""
        self.assertIO(input, output)
    def test_入力例4(self):
        input = """19
bcabcabcabcabcabcab"""
        output = """9"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()