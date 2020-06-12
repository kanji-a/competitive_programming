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
        input = """198 1.10"""
        output = """217"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 0.01"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000000000000000 9.99"""
        output = """9990000000000000"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1000000000000000 0.01"""
        output = """10000000000000"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """0 0.00"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_6(self):
        input = """1 0.00"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_7(self):
        input = """0 1.23"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_8(self):
        input = """198 1.00"""
        output = """198"""
        self.assertIO(input, output)

    def test_入力例_9(self):
        input = """198 1.01"""
        output = """199"""
        self.assertIO(input, output)

    def test_入力例_10(self):
        input = """201 1.01"""
        output = """203"""
        self.assertIO(input, output)

    def test_入力例_11(self):
        input = """101 0.99"""
        output = """99"""
        self.assertIO(input, output)

    def test_入力例_12(self):
        input = """10101010101010 0.99"""
        output = """9999999999999"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
