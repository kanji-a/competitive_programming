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
        input = """5
1 2
2 3
3 4
4 5
1 2 3 4 5"""
        output = """10
1 2 3 4 5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
1 2
1 3
1 4
1 5
3141 59 26 53 59"""
        output = """197
59 26 3141 59 53"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
