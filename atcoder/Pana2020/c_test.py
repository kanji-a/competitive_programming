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
        input = """2 3 9"""
        output = """No"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """2 3 10"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """4 9 24"""
        output = """No"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """4 9 25"""
        output = """No"""
        self.assertIO(input, output)
    def test_入力例_5(self):
        input = """4 9 26"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_入力例_6(self):
        input = """1 1 4"""
        output = """No"""
        self.assertIO(input, output)
    def test_入力例_7(self):
        input = """1 1 5"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_入力例_8(self):
        input = """100000000 100000000 1000000000"""
        output = """Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()