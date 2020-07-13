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
        input = """1 10
3 5"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 10
3 5
2 6"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 1000000000
1 1
1 10000000
1 30000000
1 99999999"""
        output = """860000004"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """5 500
35 44
28 83
46 62
31 79
40 43"""
        output = """9"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
