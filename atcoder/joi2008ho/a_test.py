from a import resolve
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
        input = """8
1
0
1
1
0
0
0
0"""
        output = """6"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """8
1
0
1
1
0
0
0
1"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """20
0
1
1
0
1
0
0
0
0
0
1
1
1
1
1
0
1
0
0
1"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """100
0
1
1
0
1
0
0
0
0
0
1
1
1
1
1
0
1
0
0
1
0
1
1
0
0
0
1
1
0
0
1
1
1
0
0
1
0
0
0
0
0
1
1
0
0
0
1
1
1
1
1
0
0
0
1
1
0
1
0
1
0
0
0
1
0
0
0
0
1
0
1
1
1
1
1
1
1
1
0
0
1
0
0
1
1
1
0
1
0
0
1
1
0
1
0
0
1
1
0
1"""
        output = """64"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()