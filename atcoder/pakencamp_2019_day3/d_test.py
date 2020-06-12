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
        input = """1
B
R
#
W
B"""
        output = """3"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3
WWR
#RW
BW#
##B
RBR"""
        output = """10"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """8
RRRRRRRR
########
BBBBBBBB
RRRRRRRR
WWWWWWWW"""
        output = """28"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """7
BR#WB#R
RWW#WRB
##WBR#W
WB#B#RW
BRW##BB"""
        output = """21"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()