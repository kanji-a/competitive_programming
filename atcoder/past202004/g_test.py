from g import resolve
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
        input = """6
1 a 5
2 3
1 t 8
1 c 10
2 21
2 4"""
        output = """9
168
0"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """4
1 x 5
1 y 8
2 7
1 z 8"""
        output = """29"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """3
1 p 3
1 q 100000
2 100000"""
        output = """9999400018"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()