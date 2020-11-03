from r import resolve
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
        input = """4 2
0 1 0 0
0 0 1 1
0 0 0 1
1 0 0 0"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 3
0 1 0
1 0 1
0 0 0"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6 2
0 0 0 0 0 0
0 0 1 0 0 0
0 0 0 0 0 0
0 0 0 0 1 0
0 0 0 0 0 1
0 0 0 0 0 0"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1 1
0"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """10 1000000000000000000
0 0 1 1 0 0 0 1 1 0
0 0 0 0 0 1 1 1 0 0
0 1 0 0 0 1 0 1 0 1
1 1 1 0 1 1 0 1 1 0
0 1 1 1 0 1 0 1 1 1
0 0 0 1 0 0 1 0 1 0
0 0 0 1 1 0 0 1 0 1
1 0 0 0 1 0 1 0 0 0
0 0 0 0 0 1 0 0 0 0
1 0 1 1 1 0 1 1 1 0"""
        output = """957538352"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
