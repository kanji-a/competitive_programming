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
        input = """3 10
3
2
1"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """4 100
1
1
1
1"""
        output = """200"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """10 1000
1
2
3
4
5
6
7
8
9
10"""
        output = """8000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
