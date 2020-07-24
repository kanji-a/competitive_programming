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

    def test_入力例1(self):
        input = """3 2"""
        output = """0.48148148148148148148"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """3 1"""
        output = """0.25925925925925925926"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """765 573"""
        output = """0.00147697396984624371"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
