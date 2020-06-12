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
2
8
1
10
9"""
        output = """18"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """8
1
10
4
5
6
2
9
3"""
        output = """26"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """15
182243672
10074562
977552215
122668426
685444213
3784162
463324752
560071245
134465220
21447865
654556327
183481051
20041805
405079805
564327789"""
        output = """3600242976"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """1
5"""
        output = """5"""
        self.assertIO(input, output)
    def test_入力例_5(self):
        input = """2
5
7"""
        output = """7"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()