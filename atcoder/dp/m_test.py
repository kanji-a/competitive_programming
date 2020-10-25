from m import resolve
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
        input = """3 4
1 2 3"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 10
9"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 0
0 0"""
        output = """1"""
        self.assertIO(input, output)

#     def test_入力例_4(self):
#         input = """4 100000
# 100000 100000 100000 100000"""
#         output = """665683269"""
#         self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()