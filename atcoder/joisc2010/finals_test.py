from finals import resolve
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
        input = """4 3 1
1 2 2
2 3 9
2 4 5"""
        output = """16"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """5 6 2
1 2 5
1 3 3
2 3 4
2 5 7
3 4 6
4 5 5"""
        output = """12"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()