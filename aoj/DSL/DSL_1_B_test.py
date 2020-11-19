from DSL_1_B import resolve
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
        input = """5 6
0 0 2 5
0 1 2 3
1 0 1
1 1 3
0 1 4 8
1 0 4"""
        output = """2
?
10"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()