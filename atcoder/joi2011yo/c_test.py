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
    def test_入力例_1(self):
        input = """11
4
5 2
9 7
4 4
3 9"""
        output = """2
3
1
3"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """16
7
3 7
5 2
11 6
15 2
9 7
8 12
15 16"""
        output = """3
2
3
2
1
2
1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()