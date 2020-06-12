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
        input = """1 2
80 84"""
        output = """84"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3 4
37 29 70 41
85 69 76 50
53 10 95 100"""
        output = """250"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """8 2
31000000 41000000
59000000 26000000
53000000 58000000
97000000 93000000
23000000 84000000
62000000 64000000
33000000 83000000
27000000 95000000"""
        output = """581000000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()