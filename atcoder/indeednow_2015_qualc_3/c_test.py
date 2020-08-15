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

    def test_入力例1(self):
        input = """4
1 3
1 4
2 3"""
        output = """1 3 2 4"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """6
1 2
2 3
2 6
6 4
1 5"""
        output = """1 2 3 5 6 4"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """7
1 5
5 2
5 3
5 7
5 6
6 4"""
        output = """1 5 2 3 6 4 7"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
