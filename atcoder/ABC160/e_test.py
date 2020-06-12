from e import resolve
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
        input = """1 2 2 2 1
2 4
5 1
3"""
        output = """12"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """2 2 2 2 2
8 6
9 1
2 1"""
        output = """25"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """2 2 4 4 4
11 12 13 14
21 22 23 24
1 2 3 4"""
        output = """74"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()