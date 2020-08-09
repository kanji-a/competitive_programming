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
        input = """3 7
9 3 4"""
        output = """POSSIBLE"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 5
6 9 3"""
        output = """IMPOSSIBLE"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 11
11 3 7 15"""
        output = """POSSIBLE"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """5 12
10 2 8 6 4"""
        output = """IMPOSSIBLE"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
