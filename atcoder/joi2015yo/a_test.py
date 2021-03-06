from a import resolve
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
        input = """9
100
20
3
10"""
        output = """90"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """8
300
100
10
250"""
        output = """1800"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()