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
        input = """5 3
1 2
3 4
5 1"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 10
1 2
2 1
1 2
2 1
1 2
1 3
1 4
2 3
2 4
3 4"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 4
3 1
4 1
5 9
2 6"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
