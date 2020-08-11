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
        input = """3"""
        output = """1 0 2 2 0 1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100"""
        output = """0 0 10 0 0 10"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """311114770564041497"""
        output = """314159265 358979323 846264338 327950288 419716939 937510582"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
