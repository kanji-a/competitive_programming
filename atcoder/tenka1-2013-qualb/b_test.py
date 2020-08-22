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
        input = """7 20
Push 2 3
Push 4 5
Top
Size
Pop 5
Top
Size"""
        output = """5
6
3
1
SAFE"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 10
Push 40 40"""
        output = """FULL"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 10
Push 1 2
Top
Pop 1
Top
Size"""
        output = """2
EMPTY"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """4 10
Top
Size
Push 1 1
Top"""
        output = """EMPTY"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
