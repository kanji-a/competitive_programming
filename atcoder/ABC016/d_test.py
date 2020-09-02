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

    def test_入力例1(self):
        input = """-2 0 2 0
4
1 1
-1 1
-1 -1
1 -1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """-3 1 3 1
8
2 2
1 2
1 0
-1 0
-1 2
-2 2
-2 -1
2 -1"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """0 1 3 1
8
2 2
1 2
1 0
-1 0
-1 2
-2 2
-2 -1
2 -1"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
