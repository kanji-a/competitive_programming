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
    def test_入力例1(self):
        input = """4 4 2
3413
4121
1424
2312"""
        output = """23"""
        self.assertIO(input, output)
    def test_入力例2(self):
        input = """4 4 2
1212
2121
1212
2121"""
        output = """54"""
        self.assertIO(input, output)
    def test_入力例3(self):
        input = """7 7 2
8989898
9898989
8989898
9898989
8989898
9898989
8989898"""
        output = """2520"""
        self.assertIO(input, output)
    def test_入力例4(self):
        input = """17 17 2
12345678912345678
23456789123456789
34567891234567891
45678912345678912
56789123456789123
67891234567891234
78912345678912345
89123456789123456
91234567891234567
12345678912345678
23456789123456789
34567891234567891
45678912345678912
56789123456789123
67891234567891234
78912345678912345
89123456789123456"""
        output = """2354638"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()