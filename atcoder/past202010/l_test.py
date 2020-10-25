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
        input = """4 2
10 20 30 20
1 10
3 4 20"""
        output = """1
2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 20
108 112 112 110 110 109 108 110 111 112
3 4 2
1 1
3 9 1
3 4 2
2 1
1 1
3 7 2
2 1
3 8 2
1 1
2 1
1 1
3 10 2
3 6 1
2 1
3 7 1
1 1
2 1
3 3 2
3 3 2"""
        output = """2
2
1
1
2
1
0
3
3
0
3
0
0
0
4
3
1
3
3
2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
