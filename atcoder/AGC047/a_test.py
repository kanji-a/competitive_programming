from a import resolve
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
        input = """5
7.5
2.4
17.000000001
17
16.000000000"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """11
0.9
1
1
1.25
2.30000
5
70
0.000000001
9999.999999999
0.999999999
1.000000001"""
        output = """8"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
