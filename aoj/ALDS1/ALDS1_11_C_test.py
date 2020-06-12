from ALDS1_11_C import resolve
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
1 2 2 4
2 1 4
3 0
4 1 3"""
        output = """1 0
2 1
3 2
4 1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()