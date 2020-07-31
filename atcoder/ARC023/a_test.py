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
        input = """1988
7
3"""
        output = """9449"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """1
1
1"""
        output = """735369"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """2014
5
16"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """2012
2
29"""
        output = """808"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
