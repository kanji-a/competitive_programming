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
3 4 6"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
7 46 11 20 11"""
        output = """90"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7
994 518 941 851 647 2 581"""
        output = """4527"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
