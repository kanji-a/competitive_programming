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

    def test_入力例_1(self):
        input = """5
2 4 1 5 3"""
        output = """4
2
3
1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
5 4 3 2 1"""
        output = """-1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
