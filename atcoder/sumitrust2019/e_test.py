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
        input = """6
0 1 2 3 4 5"""
        output = """3"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3
0 0 0"""
        output = """6"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """54
0 0 1 0 1 2 1 2 3 2 3 3 4 4 5 4 6 5 7 8 5 6 6 7 7 8 8 9 9 10 10 11 9 12 10 13 14 11 11 12 12 13 13 14 14 15 15 15 16 16 16 17 17 17"""
        output = """115295190"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """6
0 1 0 0 1 2"""
        output = """24"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()