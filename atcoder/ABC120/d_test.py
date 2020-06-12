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
        input = """4 5
1 2
3 4
1 3
2 3
1 4"""
        output = """0
0
4
5
6"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """6 5
2 3
1 2
5 6
3 4
4 5"""
        output = """8
9
12
14
15"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """2 1
1 2"""
        output = """1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()