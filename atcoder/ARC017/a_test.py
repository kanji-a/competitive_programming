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

    def test_入力例１(self):
        input = """17"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例２(self):
        input = """18"""
        output = """NO"""
        self.assertIO(input, output)

    def test_入力例３(self):
        input = """999983"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例４(self):
        input = """672263"""
        output = """NO"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
