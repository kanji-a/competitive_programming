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
        input = """5
1
7
9
6
10"""
        output = """3
0"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """10
8
7
14
18
4
11
3
17
5
19"""
        output = """2
0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()