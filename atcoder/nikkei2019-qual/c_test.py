from c import resolve
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
        input = """3
10 10
20 20
30 30"""
        output = """20"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
20 10
20 20
20 30"""
        output = """20"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
1 1000000000
1 1000000000
1 1000000000
1 1000000000
1 1000000000
1 1000000000"""
        output = """-2999999997"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
