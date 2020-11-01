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
        input = """2
0 -40
0 40"""
        output = """40"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
0 -10
99 10
0 91
99 -91"""
        output = """50.5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
-90 40
20 -30
0 -90
10 -70
80 70
-90 30
-20 -80
10 90
50 30
60 -70"""
        output = """33.541019662496845446"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10
65 -90
-34 -2
62 99
42 -13
47 -84
84 87
16 -78
56 35
90 8
90 19"""
        output = """35.003571246374276203"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
