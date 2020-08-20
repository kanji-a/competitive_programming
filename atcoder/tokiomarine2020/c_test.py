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
        input = """5 1
1 0 0 1 0"""
        output = """1 2 2 1 2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 2
1 0 0 1 0"""
        output = """3 3 4 4 3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """20 20
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0"""
        output = """20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
