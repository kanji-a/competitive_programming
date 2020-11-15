from f import resolve
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
        input = """5 5
1 2 3 2 1
1 1 2
1 2 5
2 1 1
1 3 4
2 3 4"""
        output = """2
0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 4
2 2 2 2 2
1 1 2
1 1 3
1 2 3
2 2 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """12 9
1 2 3 1 2 3 1 2 3 1 2 3
1 1 2
1 3 4
1 5 6
1 7 8
2 2 1
1 9 10
2 5 6
1 4 8
2 6 1"""
        output = """1
0
0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
