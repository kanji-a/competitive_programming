from h import resolve
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
        input = """3 4 3
1123
1214
1810"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8 6 40
846444
790187
264253
967004
578258
204367
681998
034243"""
        output = """6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
