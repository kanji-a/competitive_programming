from DPL_1_G import resolve
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
        input = """4 8
4 3 2
2 1 1
1 2 4
3 2 2"""
        output = """12"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """2 100
1 1 100
2 1 50"""
        output = """150"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()