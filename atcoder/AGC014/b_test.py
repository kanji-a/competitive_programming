from b import resolve
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
        input = """4 4
1 2
2 4
1 3
3 4"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 5
1 2
3 5
5 1
3 4
2 3"""
        output = """NO"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
