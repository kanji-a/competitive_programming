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
        input = """6 2
abcde
caac
abcde
caac
abc
caac"""
        output = """abcde"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """9 3
a
a
bb
bb
a
ccc
bb
ccc
dddd"""
        output = """ccc"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7 2
caac
abcde
caac
abc
abcde
caac
abc"""
        output = """AMBIGUOUS"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
