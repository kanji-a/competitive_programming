from c import resolve
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
        input = """1 0 1
2 1 2
1 0 1"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """2 2 2
2 1 2
2 2 2"""
        output = """No"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """0 8 8
0 8 8
0 8 8"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """1 8 6
2 9 7
0 7 7"""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()