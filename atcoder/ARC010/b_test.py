from b import resolve
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
        input = """1
1/9"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1
1/10"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1
1/7"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """2
1/7
1/9"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """2
12/29
12/30"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
