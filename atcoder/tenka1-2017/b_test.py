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
        input = """3
4 7
2 9
6 2"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
1 10
3 6
5 2
4 4
2 8"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
1 1000000000
1000000000 1"""
        output = """1000000001"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
