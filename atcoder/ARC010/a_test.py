from a import resolve
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
        input = """100 3 0 100
10
20
30"""
        output = """complete"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100 4 0 100
10
20
30
40"""
        output = """complete"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100 4 0 100
50
40
30
20"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """100 4 10 100
50
40
30
20"""
        output = """complete"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """5 3 20 10
15
5
20"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
