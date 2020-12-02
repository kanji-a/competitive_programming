from c import resolve
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
        input = """5 1"""
        output = """1 10
8 12
13 20
11 14
2 4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 -10"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6 2"""
        output = """2 7
3 6
4 5
8 9
10 11
1 12"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
