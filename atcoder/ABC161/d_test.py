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
        input = """15"""
        output = """23"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """1"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """13"""
        output = """21"""
        self.assertIO(input, output)
    # def test_入力例_5(self):
    #     input = """1000"""
    #     output = """8888888888"""
    #     self.assertIO(input, output)
    def test_入力例_4(self):
        input = """100000"""
        output = """3234566667"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()