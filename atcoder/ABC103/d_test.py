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
1 4
2 5"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """9 5
1 8
2 7
3 5
4 6
7 9"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 10
1 2
1 3
1 4
1 5
2 3
2 4
2 5
3 4
3 5
4 5"""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
