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
        input = """2 1 6
2 1 1
1 1
1 2
2 2 1
1 1
1 2"""
        output = """1
0
0
0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 5 30
1 3
2 3 5
1 3
2 2 1
2 4 5
2 5 2
2 2 3
1 4
2 4 1
2 2 2
1 1
1 5
2 5 3
2 4 4
1 4
1 2
2 3 3
2 4 3
1 3
1 5
1 3
2 1 3
1 1
2 2 4
1 1
1 4
1 5
1 4
1 1
1 5"""
        output = """0
4
3
0
3
10
9
4
4
4
0
0
9
3
9
0
3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
