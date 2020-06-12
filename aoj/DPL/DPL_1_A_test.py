from DPL_1_A import resolve
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
        input = """55 4
1 5 10 50"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """15 6
1 2 7 8 12 50"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """65 6
1 2 7 8 12 50"""
        output = """3"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """100 6
1 72 93 34 24 37"""
        output = """5"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()