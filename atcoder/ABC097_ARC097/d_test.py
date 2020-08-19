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

    def test_入力例_1(self):
        input = """5 2
5 3 1 4 2
1 3
5 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 2
3 2 1
1 2
2 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 8
5 3 6 8 7 10 9 1 2 4
3 1
4 1
5 9
2 5
6 5
3 5
8 9
7 9"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """5 1
1 2 3 4 5
1 5"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
