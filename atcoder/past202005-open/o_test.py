from o import resolve
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
        input = """2 1
3 2
3 3
100000 100000 100000"""
        output = """81"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 2
2 4 3 3
4 2 3 3
100000 100000 100000"""
        output = """210"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """20 19
3 2 3 4 3 3 2 3 2 2 3 3 4 3 2 4 4 3 3 4
2 3 4 2 4 3 3 2 4 2 4 3 3 2 3 4 4 4 2 2
3 4 5"""
        output = """-1417"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
