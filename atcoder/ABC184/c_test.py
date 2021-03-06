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
        input = """1 1
5 6"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 1
1 200001"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 3
998244353 998244853"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1 1
1 1"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
