from c import resolve
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
        input = """3 5 3
5
1 2
2 1
2 5
3 2
3 5"""
        output = """5"""
        self.assertIO(input, output)
    def test_入力例2(self):
        input = """7 3 1
4
3 2
3 3
4 2
4 3"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例3(self):
        input = """5 5 2
5
1 1
2 2
3 3
4 4
5 5"""
        output = """20"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()