# from l import resolve
from l_acl import resolve
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
        input = """3 1
0 0 1
0 1 1
1 0 1
1 1 1"""
        output = """2.000000000000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 1
0 10 1
10 0 2
10 20 3
10 10 1"""
        output = """210.000000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
