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

    def test_入力例1(self):
        input = """ab*"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """abc"""
        output = """NO"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """a*bc*"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """***"""
        output = """YES"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
