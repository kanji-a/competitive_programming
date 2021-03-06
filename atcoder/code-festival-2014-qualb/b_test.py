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

    def test_入力例1(self):
        input = """6 100
30
10
40
10
50
10"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """6 200
100
100
100
100
100
100"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
