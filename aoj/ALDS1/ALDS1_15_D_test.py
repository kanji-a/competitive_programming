from ALDS1_15_D import resolve
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
        input = """abca"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """aaabbcccdeeeffg"""
        output = """41"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """z"""
        output = """1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()