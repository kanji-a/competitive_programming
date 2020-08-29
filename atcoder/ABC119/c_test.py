from c import resolve
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
        input = """5 100 90 80
98
40
30
21
80"""
        output = """23"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8 100 90 80
100
100
90
90
90
80
80
80"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8 1000 800 100
300
333
400
444
500
555
600
666"""
        output = """243"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
