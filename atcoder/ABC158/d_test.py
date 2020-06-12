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
    def test_入力例_1(self):
        input = """a
4
2 1 p
1
2 2 c
1"""
        output = """cpa"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """a
6
2 2 a
2 1 b
1
2 2 c
1
1"""
        output = """aabc"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """y
1
2 1 x"""
        output = """xy"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()