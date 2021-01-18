from o import resolve
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
        input = """2
1 2 3 4 5 6
7 8 9 10 11 12"""
        output = """3.64925355954377"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
12 237 374 111 247 234
857 27 98 65 83 90
764 60 999 11 7 4"""
        output = """3.42188884244970"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
