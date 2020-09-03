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

    def test_入力例１(self):
        input = """3
1 1
1 2
3 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """3
1 1
1 2
2 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """3
1 1
2 2
3 3"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """8
3 1
4 1
5 9
2 6
5 3
5 8
9 7
9 3"""
        output = """38"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
