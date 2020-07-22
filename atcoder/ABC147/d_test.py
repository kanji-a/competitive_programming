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
        input = """3
1 2 3"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
3 1 4 1 5 9 2 6 5 3"""
        output = """237"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
3 14 159 2653 58979 323846 2643383 27950288 419716939 9375105820"""
        output = """103715602"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
