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
        input = """5 5
3 4"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例2(self):
        input = """10 20
2 2"""
        output = """10"""
        self.assertIO(input, output)
    def test_入力例3(self):
        input = """1 1
2 2"""
        output = """0"""
        self.assertIO(input, output)
#     def test_入力例4(self):
#         input = """10000000000 10000000000
# 4 3"""
#         output = """4545454545"""
#         self.assertIO(input, output)
#     def test_入力例5(self):
#         input = """100 100
# 4 3"""
#         output = """0"""
        self.assertIO(input, output)
#     def test_入力例6(self):
#         input = """100 100
# 4 3"""
#         output = """0"""
#         self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()