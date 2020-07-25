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

    def test_入力例1(self):
        input = """3 3
010
101
010"""
        output = """000
010
000"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """3 4
0230
2323
0230"""
        output = """0000
0230
0000"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """5 5
00100
03040
20903
05060
00300"""
        output = """00000
00100
02030
00300
00000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
