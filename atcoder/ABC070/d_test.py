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
1 2 1
1 3 1
2 4 1
3 5 1
3 1
2 4
2 3
4 5"""
        output = """3
2
4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7
1 2 1
1 3 3
1 4 5
1 5 7
1 6 9
1 7 11
3 2
1 3
4 5
6 7"""
        output = """5
14
22"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
1 2 1000000000
2 3 1000000000
3 4 1000000000
4 5 1000000000
5 6 1000000000
6 7 1000000000
7 8 1000000000
8 9 1000000000
9 10 1000000000
1 1
9 10"""
        output = """17000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
