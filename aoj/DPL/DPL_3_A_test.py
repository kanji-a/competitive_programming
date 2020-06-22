from DPL_3_A import resolve
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
0 0 1 0 0
1 0 0 0 0
0 0 0 1 0
0 0 0 1 0"""
        output = """4"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()