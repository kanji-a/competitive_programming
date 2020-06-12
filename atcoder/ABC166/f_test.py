from f import resolve
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
        input = """2 1 3 0
AB
AC"""
        output = """Yes
A
C"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3 1 0 0
AB
BC
AB"""
        output = """No"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """1 0 9 0
AC"""
        output = """No"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """8 6 9 1
AC
BC
AB
BC
AC
BC
AB
AB"""
        output = """Yes
C
B
B
C
C
B
A
A"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()