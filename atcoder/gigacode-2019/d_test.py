from d2 import resolve
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
        input = """1 1 200 500
300"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """1 8 10 200
30 40 10 20 30 40 10 20"""
        output = """6"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """5 5 10 17
12 19 25 13 25
14 16 18 11 10
19 17 24 26 12
23 11 16 19 14
18 23 27 11 16"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """4 7 10 240
17 12 15 18 19 15 23
22 12 41 16 27 10 10
15 69 18 11 10 23 15
12 20 13 12 17 18 15"""
        output = """9"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()