from c import resolve
import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    maxDiff = None
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """4
2 3 5
2 1 5
1 2 5
3 2 5"""
        output = """2 2 6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
0 0 100
1 1 98"""
        output = """0 0 100"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
99 1 191
100 1 192
99 0 192"""
        output = """100 0 193"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
