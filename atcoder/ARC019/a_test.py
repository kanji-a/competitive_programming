from a import resolve
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
        input = """1Z0"""
        output = """120"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """4ZD6O"""
        output = """42060"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """BI9Z"""
        output = """8192"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
