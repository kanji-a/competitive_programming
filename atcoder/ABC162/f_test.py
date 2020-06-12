from f import resolve
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
        input = """6
1 2 3 4 5 6"""
        output = """12"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """5
-1000 -100 -10 0 10"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """10
1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000"""
        output = """5000000000"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """27
18 -28 18 28 -45 90 -45 23 -53 60 28 -74 -71 35 -26 -62 49 -77 57 24 -70 -93 69 -99 59 57 -49"""
        output = """295"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()