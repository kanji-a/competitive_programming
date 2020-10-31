from l import resolve
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
10 80 90 30"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
10 100 10"""
        output = """-80"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1
10"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10
1000000000 1 1000000000 1 1000000000 1 1000000000 1 1000000000 1"""
        output = """4999999995"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """6
4 2 9 7 1 5"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
