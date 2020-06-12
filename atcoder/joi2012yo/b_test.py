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
    def test_入力例_1(self):
        input = """4
1 2 0 1
1 3 2 1
1 4 2 2
2 3 1 1
2 4 3 0
3 4 1 3"""
        output = """2
1
4
2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """5
1 2 1 1
3 4 3 1
5 1 1 2
2 3 0 0
4 5 2 3
1 3 0 2
5 2 2 2
4 1 4 5
3 5 4 0
2 4 0 1"""
        output = """2
4
1
4
3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()