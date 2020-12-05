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
        input = """4
1011"""
        output = """9999999999"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """22
1011011011011011011011"""
        output = """9999999993"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
11"""
        output = """10000000000"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1
1"""
        output = """20000000000"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """1
0"""
        output = """10000000000"""
        self.assertIO(input, output)

    def test_入力例_6(self):
        input = """3
111"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_7(self):
        input = """4
0110"""
        output = """9999999999"""
        self.assertIO(input, output)

    def test_入力例_8(self):
        input = """6
111011"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_9(self):
        input = """6
110111"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_10(self):
        input = """2
00"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_11(self):
        input = """3
110"""
        output = """10000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
