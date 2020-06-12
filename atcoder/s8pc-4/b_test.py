from b import resolve
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
        input = """5 5
3949 3774 3598 3469 3424"""
        output = """1541"""
        self.assertIO(input, output)
    def test_入力例2(self):
        input = """5 3
7 4 2 6 4"""
        output = """7"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()