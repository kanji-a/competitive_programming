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
        input = """abcdefgh
3"""
        output = """adg"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """lllll
1"""
        output = """lllll"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """souuundhound
2"""
        output = """suudon"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
