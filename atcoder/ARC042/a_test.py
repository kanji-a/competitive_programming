from a import resolve
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
        input = """3 3
2
3
1"""
        output = """1
3
2"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """3 3
1
1
1"""
        output = """1
2
3"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """10 10
3
1
4
1
5
9
2
6
5
3"""
        output = """3
5
6
2
9
1
4
7
8
10"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
