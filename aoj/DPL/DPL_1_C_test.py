from DPL_1_C import resolve
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
        input = """4 8
4 2
5 2
2 1
8 3"""
        output = """21"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """2 20
5 9
4 10"""
        output = """10"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """3 9
2 1
3 1
5 2"""
        output = """27"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()