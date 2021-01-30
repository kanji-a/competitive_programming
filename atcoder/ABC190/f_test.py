from f import resolve
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
0 1 2 3"""
        output = """0
3
4
3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
0 3 1 5 4 2 9 6 8 7"""
        output = """9
18
21
28
27
28
33
24
21
14"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
