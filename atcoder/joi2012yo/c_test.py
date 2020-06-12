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
        input = """3
12 2
200
50
300
100"""
        output = """37"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """4
20 3
900
300
100
400
1300"""
        output = """100"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()