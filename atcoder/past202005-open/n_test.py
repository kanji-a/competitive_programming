from n import resolve
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
        input = """5 3
1 1 0
1 2 0
2 2 4"""
        output = """2 1 3 4 5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 15
1 3 0
1 5 0
1 4 0
1 2 0
1 3 0
2 4 7
1 5 0
1 7 0
1 9 0
1 8 0
2 3 5
1 8 0
1 9 0
1 5 0
1 2 0"""
        output = """1 2 4 5 3 6 8 7 9 10"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
