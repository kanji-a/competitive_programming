from d_rec import resolve
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
    def test_入力例1(self):
        input = """1 9"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例2(self):
        input = """40 49"""
        output = """10"""
        self.assertIO(input, output)
    def test_入力例3(self):
        input = """1 1000"""
        output = """488"""
        self.assertIO(input, output)
    def test_入力例4(self):
        input = """1 1000000000000000000"""
        output = """981985601490518016"""
        self.assertIO(input, output)
    def test_入力例5(self):
        input = """1 357"""
        output = """127"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()