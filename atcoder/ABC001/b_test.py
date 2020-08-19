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

    def test_入力例_1(self):
        input = """15000"""
        output = """65"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """75000"""
        output = """89"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """200"""
        output = """02"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
