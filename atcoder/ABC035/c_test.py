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
        input = """5 4
1 4
2 5
3 3
1 5"""
        output = """01010"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """20 8
1 8
4 13
8 8
3 18
5 20
19 20
2 7
4 9"""
        output = """10110000011110000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
