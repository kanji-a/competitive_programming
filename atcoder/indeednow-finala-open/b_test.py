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

    def test_入力例1(self):
        input = """3 4
s120
0321
220t"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """5 5
s0010
12032
11303
12114
5001t"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """1 2
st"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """2 1
s
t"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
