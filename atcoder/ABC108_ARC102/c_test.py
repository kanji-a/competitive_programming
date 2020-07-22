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
        input = """3 2"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """31415 9265"""
        output = """27"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """35897 932"""
        output = """114191"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
