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
        input = """5
2 5
1 5
2 4
3 2"""
        output = """14"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """10
7 9
8 1
9 6
10 8
8 6
10 3
5 8
4 8
2 5"""
        output = """192"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
