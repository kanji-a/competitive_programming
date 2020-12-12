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
        input = """abc"""
        output = """bbb"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """zzzzzzzzzzzzzzzzzzzz"""
        output = """NO"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """abcdef"""
        output = """fedcba"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """k"""
        output = """bbbbba"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """aa"""
        output = """b"""
        self.assertIO(input, output)

    def test_入力例_6(self):
        input = """bb"""
        output = """aba"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
