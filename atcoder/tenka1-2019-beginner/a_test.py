from a import resolve
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
        input = """3 8 5"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 3 1"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 2 4"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """31 41 59"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
