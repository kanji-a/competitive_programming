from d import resolve
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
        input = """4 4
1 4
3 3
6 2
8 1"""
        output = """21"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 2
0 0
1 1
2 2
3 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 3
-1000000000 -1000000000
1000000000 1000000000
-999999999 999999999
999999999 -999999999"""
        output = """3999999996000000001"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
