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
        input = """3 2 1
9 5
3 1
8 9"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """4 4 100
999 999 999 999
999 999 999 999
999 999 999 999
999 999 999 999"""
        output = """999"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """3 4 5
700 198 700 198
198 700 198 700
700 198 700 198"""
        output = """198"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
