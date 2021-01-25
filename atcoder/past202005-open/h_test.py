from h import resolve
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
        input = """2 5
1 4
2 2 20"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 5
1 2 3 4
2 20 100"""
        output = """164"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 19
1 3 4 5 7 8 10 13 15 17
2 1000 10"""
        output = """138"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
