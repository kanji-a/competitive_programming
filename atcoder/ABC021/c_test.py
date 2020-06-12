from c import resolve
import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    maxDiff = None
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例1(self):
        input = """7
1 7
8
1 2
1 3
4 2
4 3
4 5
4 6
7 5
7 6"""
        output = """4"""
        self.assertIO(input, output)
    def test_入力例2(self):
        input = """7
1 7
9
1 2
1 3
4 2
4 3
4 5
4 6
7 5
7 6
4 7"""
        output = """2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()