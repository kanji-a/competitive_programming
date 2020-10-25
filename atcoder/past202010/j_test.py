from j import resolve
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
        input = """3 2
10 10 10
ABA
1 2 15
2 3 5"""
        output = """15"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 2
10 1000000000 10
ABC
1 2 1000000000
2 3 1000000000"""
        output = """20"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 6
5 10 15
ABCBC
5 4 4
3 5 2
1 3 7
3 4 1
4 2 1
2 3 3"""
        output = """8"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
