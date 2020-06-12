from d import resolve
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
        input = """10
2"""
        output = """55"""
        self.assertIO(input, output)
    def test_入力例2(self):
        input = """10
3"""
        output = """220"""
        self.assertIO(input, output)
    def test_入力例3(self):
        input = """10
4"""
        output = """715"""
        self.assertIO(input, output)
    def test_入力例4(self):
        input = """400
296"""
        output = """546898535"""
        self.assertIO(input, output)
    def test_入力例5(self):
        input = """100000
100000"""
        output = """939733670"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()