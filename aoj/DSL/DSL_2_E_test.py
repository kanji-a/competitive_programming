from DSL_2_E import resolve
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
        input = """3 5
0 1 2 1
0 2 3 2
0 3 3 3
1 2
1 3"""
        output = """3
5"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """4 3
1 2
0 1 4 1
1 2"""
        output = """0
1"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """1 3
1 1
0 1 1 1
1 1"""
        output = """0
1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()