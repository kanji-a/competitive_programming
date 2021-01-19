from k import resolve
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
))(
3 5 7
2 6 5"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1
(
10
20"""
        output = """20"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
))())((()(
13 18 17 3 20 20 6 14 14 2
20 1 19 5 2 19 2 19 9 4"""
        output = """18"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """4
()()
17 8 3 19
5 3 16 3"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
