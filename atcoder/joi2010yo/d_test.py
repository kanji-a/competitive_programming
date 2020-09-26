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
        input = """4
2
1
2
12
1"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
3
72
2
12
7
2
1"""
        output = """68"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
