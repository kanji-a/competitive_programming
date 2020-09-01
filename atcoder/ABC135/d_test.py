from d import resolve
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
        input = """??2??5"""
        output = """768"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """?44"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7?4"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """?6?42???8??2??06243????9??3???7258??5??7???????774????4?1??17???9?5?70???76???"""
        output = """153716888"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
