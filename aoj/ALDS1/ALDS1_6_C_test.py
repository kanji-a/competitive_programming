from ALDS1_6_C import resolve
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
        input = """6
D 3
H 2
D 1
S 3
D 2
C 1"""
        output = """Not stable
D 1
C 1
D 2
H 2
D 3
S 3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
S 1
H 1"""
        output = """Stable
S 1
H 1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """12
H 3
S 3
D 3
C 3
H 1
S 1
D 1
H 2
C 1
S 2
D 2
C 2"""
        output = """Stable
H 1
S 1
D 1
C 1
H 2
S 2
D 2
C 2
H 3
S 3
D 3
C 3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()