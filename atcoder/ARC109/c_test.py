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
        input = """3 2
RPS"""
        output = """P"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """11 1
RPSSPRSPPRS"""
        output = """P"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 100
S"""
        output = """S"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """3 3
RPS"""
        output = """S"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """1 3
S"""
        output = """S"""
        self.assertIO(input, output)

#     def test_入力例_6(self):
#         input = """100 100 
# SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS"""
#         output = """S"""
#         self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
