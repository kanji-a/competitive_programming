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
        input = """4 5
3 2 4 1"""
        output = """4"""
        self.assertIO(input, output)
    def test_入力例_8(self):
        input = """4 6
3 2 4 1"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """6 727202214173249351
6 5 2 5 3 2"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """4 1
3 2 4 1"""
        output = """3"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """6 1
6 5 2 5 3 2"""
        output = """6"""
        self.assertIO(input, output)
    def test_入力例_5(self):
        input = """6 2
6 5 2 5 3 2"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_6(self):
        input = """3 2
1 3 2"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例_7(self):
        input = """2 2
2 2"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_9(self):
        input = """4 5
2 3 4 1"""
        output = """2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()