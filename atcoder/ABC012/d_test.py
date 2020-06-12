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
    def test_入力例1(self):
        input = """3 2
1 2 10
2 3 10"""
        output = """10"""
        self.assertIO(input, output)
    def test_入力例2(self):
        input = """5 5
1 2 12
2 3 14
3 4 7
4 5 9
5 1 18"""
        output = """26"""
        self.assertIO(input, output)
    def test_入力例3(self):
        input = """4 6
1 2 1
2 3 1
3 4 1
4 1 1
1 3 1
4 2 1"""
        output = """1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()