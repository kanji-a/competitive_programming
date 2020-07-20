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

    def test_入力例1(self):
        input = """3 4
1 3 5 17
2 4 2 3
1 3 2 9"""
        output = """Found"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """5 3
89 62 15
44 36 17
4 24 24
25 98 99
66 33 57"""
        output = """Nothing"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
