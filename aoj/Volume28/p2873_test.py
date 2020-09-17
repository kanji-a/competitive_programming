from p2199 import resolve
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
    def test_入力例_1(self):
        input = """ brainfuck
1
fuck """
        output = """1"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """aaa
1
a"""
        output = """3
"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """hellshakeyano
3
hell
shake
key"""
        output = """3
"""
        self.assertIO(input, output)
