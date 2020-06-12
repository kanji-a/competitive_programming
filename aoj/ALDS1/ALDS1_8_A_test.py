from ALDS1_8_A import resolve
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
        input = """8
insert 30
insert 88
insert 12
insert 1
insert 20
insert 17
insert 25
print"""
        output = """ 1 12 17 20 25 30 88
 30 12 1 20 17 25 88"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """11
insert 8
insert 2
insert 3
insert 7
insert 22
insert 1
insert 10
insert 9
insert 15
insert 13
print"""
        output = """ 1 2 3 7 8 9 10 13 15 22
 8 2 1 3 7 22 10 9 15 13"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """6
insert 8
insert 2
insert 3
insert 7
insert 22
print"""
        output = """"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()