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
        input = """100 3"""
        output = """33.33"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """42 0"""
        output = """ERROR"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 2"""
        output = """2.00"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """2 3"""
        output = """0.66"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """1 1000"""
        output = """0.00"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
