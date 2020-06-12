from p1127 import resolve
import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    maxDiff = None
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """3
10.000 10.000 50.000 10.000
40.000 10.000 50.000 10.000
40.000 40.000 50.000 10.000
2
30.000 30.000 30.000 20.000
40.000 40.000 40.000 20.000
5
5.729 15.143 3.996 25.837
6.013 14.372 4.818 10.671
80.115 63.292 84.477 15.120
64.095 80.924 70.029 14.881
39.472 85.116 71.369 5.553
0"""
        output = """20.000
0.000
73.834"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()