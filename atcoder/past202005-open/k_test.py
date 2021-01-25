from k import resolve
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
        input = """3 4
1 2 1
2 3 2
3 1 3
1 3 2"""
        output = """3
3
1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 20
3 6 3
6 5 6
10 8 10
5 7 3
1 3 1
4 10 4
5 4 6
10 7 4
7 9 3
9 8 4
8 1 4
3 7 1
2 3 2
9 8 3
8 1 10
8 2 8
9 10 9
2 1 8
4 9 6
1 7 4"""
        output = """7
3
7
7
5
9
7
7
10
7"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
