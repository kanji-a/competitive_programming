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
        input = """-1 -1 2
2 3 4 5"""
        output = """YES
YES"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """0 1 1
-2 0 4 3"""
        output = """NO
YES"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """0 0 5
-2 -2 2 1"""
        output = """YES
NO"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """0 0 2
0 0 4 4"""
        output = """YES
YES"""
        self.assertIO(input, output)

    def test_入力例5(self):
        input = """0 0 5
-4 -4 4 4"""
        output = """YES
YES"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
