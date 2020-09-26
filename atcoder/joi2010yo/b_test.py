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
        input = """10 5
0
0
5
6
-3
8
1
8
-4
0
1
3
5
1
5"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 10
0
-1
-1
4
4
-5
0
1
-6
0
1
5
2
4
6
5
5
4
1
6"""
        output = """6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
