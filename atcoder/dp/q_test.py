from q import resolve
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
        input = """4
3 1 4 2
10 20 30 40"""
        output = """60"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1
1
10"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
1 2 3 4 5
1000000000 1000000000 1000000000 1000000000 1000000000"""
        output = """5000000000"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """9
4 2 5 8 3 6 1 7 9
6 8 8 4 6 3 5 7 5"""
        output = """31"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
