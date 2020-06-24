from DPL_5_A import resolve
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
        input = """2 3"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 5"""
        output = """9765625"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100 100"""
        output = """424090053"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
