from c import resolve
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
        input = """2 2 3
1 1 X
2 1 R
2 2 R"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 3 5
2 3 D
1 3 D
2 1 D
1 2 X
3 1 R"""
        output = """150"""
        self.assertIO(input, output)

#     def test_入力例_3(self):
#         input = """5000 5000 10
# 585 1323 R
# 2633 3788 X
# 1222 4989 D
# 1456 4841 X
# 2115 3191 R
# 2120 4450 X
# 4325 2864 X
# 222 3205 D
# 2134 2388 X
# 2262 3565 R"""
#         output = """139923295"""
#         self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
