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
        input = """6 2
10 30
20 60
10 10
30 100
50 140
40 120
10 3
30 1"""
        output = """3.0000000000000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 2
1 20
1 3
32 100
1 1
1 2
2 5
10 100
96 874"""
        output = """9.0000000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
