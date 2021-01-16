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
        input = """4 2
0 1 0 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 2
0 1 1 2 3"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """20 4
6 2 6 8 4 5 5 8 4 1 7 8 0 3 6 1 1 8 3 0"""
        output = """11"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """6 3
0 0 0 1 1 2"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """6 2
0 0 0 1 1 2"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_6(self):
        input = """4 1
0 1 3 5"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_7(self):
        input = """4 3
0 0 0 1"""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
