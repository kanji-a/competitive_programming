from b import resolve
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
        input = """4 5"""
        output = """10"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """7 3"""
        output = """11"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """1000000000 1000000000"""
        output = """500000000000000000"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """1 1"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例_5(self):
        input = """1 5"""
        output = """1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()