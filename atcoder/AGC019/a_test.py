from a import resolve
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
        input = """20 30 70 90
3"""
        output = """150"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10000 1000 100 10
1"""
        output = """100"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 100 1000 10000
1"""
        output = """40"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """12345678 87654321 12345678 87654321
123456789"""
        output = """1524157763907942"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
