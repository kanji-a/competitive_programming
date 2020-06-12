from d import resolve
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
        input = """3 5
10
25
15
50
30
15
40
30"""
        output = """1125"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """2 6
99
20
490
612
515
131
931
1000"""
        output = """31589"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()