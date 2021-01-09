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

    def test_入力例_1(self):
        input = """4
1 2
1 3
4 2
2 3"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
111 111
111 111"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """12
5 2
5 6
1 2
9 7
2 7
5 5
4 2
6 7
2 2
7 8
9 7
1 8"""
        output = """8"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
