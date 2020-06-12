from e import resolve
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
        input = """3
1 2
-1 1
2 -1"""
        output = """5"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """10
3 2
3 2
-1 1
2 -1
-3 -9
-8 12
7 7
8 1
8 2
8 4"""
        output = """479"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """5
0 0
0 0
1 2
-1 1
2 -1"""
        output = """7"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """4
0 0
0 2
0 1
2 0"""
        output = """5"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()