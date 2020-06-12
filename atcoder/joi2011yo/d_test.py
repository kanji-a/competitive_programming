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
        input = """11
8 3 2 4 8 7 2 4 0 8 8"""
        output = """10"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """40
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 1 1"""
        output = """7069052760"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """3
0 0 0"""
        output = """2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()