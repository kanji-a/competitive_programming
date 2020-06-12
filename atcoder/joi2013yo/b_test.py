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
        input = """5
100 99 98
100 97 92
63 89 63
99 99 99
89 97 98"""
        output = """0
92
215
198
89"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3
89 92 77
89 92 63
89 63 77"""
        output = """0
63
63"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()