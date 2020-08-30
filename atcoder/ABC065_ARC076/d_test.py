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
        input = """3
1 5
3 9
7 8"""
        output = """3"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """6
8 3
4 9
12 19
18 1
13 5
7 6"""
        output = """8"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()