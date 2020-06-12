from d import resolve
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
31
27
35
20 25 30
23 29 90
21 35 60
28 33 40"""
        output = """80"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """5 2
26
28
32
29
34
30 35 0
25 30 100"""
        output = """300"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()