from DPL_5_J import resolve
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
        input = """5 3"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 5"""
        output = """30"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100 100"""
        output = """190569292"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
