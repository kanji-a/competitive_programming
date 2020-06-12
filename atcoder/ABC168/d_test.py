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
        input = """4 4
1 2
2 3
3 4
4 2"""
        output = """Yes
1
2
2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """6 9
3 4
6 1
2 4
5 3
4 6
1 5
6 2
4 5
5 6"""
        output = """Yes
6
5
5
1
1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()