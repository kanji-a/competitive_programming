from l import resolve
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
        input = """5 5
0 1 0 0 1
2 1 5
1 3 4
2 2 5
1 1 3
2 1 2"""
        output = """2
0
1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
