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
        input = """11 2"""
        output = """4"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """1010101 10"""
        output = """7"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """314159265 3"""
        output = """18"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """1 2"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例_5(self):
        input = """2 2"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_6(self):
        input = """1000000000 10"""
        output = """10"""
        self.assertIO(input, output)
    def test_入力例_7(self):
        input = """4 2"""
        output = """3"""
        self.assertIO(input, output)
    def test_入力例_8(self):
        input = """1 10"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例_9(self):
        input = """1000000000 2"""
        output = str(len('111011100110101100101000000000'))
        self.assertIO(input, output)
    def test_入力例_10(self):
        input = """3 2"""
        output = """2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()