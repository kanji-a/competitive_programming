from f import resolve
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
        input = """5 17
2 3 5 7 11"""
        output = """17"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 100
1 2 7 5 8 10"""
        output = """33"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6 100
101 102 103 104 105 106"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """7 273599681
6706927 91566569 89131517 71069699 75200339 98298649 92857057"""
        output = """273555143"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
