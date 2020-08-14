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
        input = """3
7 6 8"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
12 15 18"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
1000000000 1000000000"""
        output = """1000000000"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """3
44 140 572"""
        output = """44"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
