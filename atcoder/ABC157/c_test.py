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
        input = """3 3
1 7
3 2
1 7"""
        output = """702"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3 2
2 1
2 3"""
        output = """-1"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """3 1
1 0"""
        output = """-1"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """1 1
1 0"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_5(self):
        input = """1 0"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_6(self):
        input = """2 0"""
        output = """10"""
        self.assertIO(input, output)
    def test_入力例_7(self):
        input = """2 1
2 0"""
        output = """10"""
    def test_入力例_8(self):
        input = """3 1
3 1"""
        output = """101"""

if __name__ == "__main__":
    unittest.main()