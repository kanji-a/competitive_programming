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
        input = """1
1024"""
        output = """1024
1024"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
3
4
5"""
        output = """12
0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
512
512"""
        output = """1024
0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """3
4
8
1"""
        output = """13
3"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """10
1
2
3
4
5
6
7
8
9
10"""
        output = """55
0"""
        self.assertIO(input, output)

    def test_入力例_6(self):
        input = """5
1
1
5
1
1"""
        output = """9
1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
