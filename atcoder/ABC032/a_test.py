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
        input = """2
3
8"""
        output = """12"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """2
2
2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """12
8
25"""
        output = """48"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
