from GRL_1_C import resolve
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
        input = """4 6
0 1 1
0 2 5
1 2 2
1 3 4
2 3 1
3 2 7"""
        output = """0 1 3 4
INF 0 2 3
INF INF 0 1
INF INF 7 0"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """4 6
0 1 1
0 2 -5
1 2 2
1 3 4
2 3 1
3 2 7"""
        output = """0 1 -5 -4
INF 0 2 3
INF INF 0 1
INF INF 7 0"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """4 6
0 1 1
0 2 5
1 2 2
1 3 4
2 3 1
3 2 -7"""
        output = """NEGATIVE CYCLE"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()