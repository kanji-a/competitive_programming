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

    def test_入力例1(self):
        input = """7
...oooo
oo.....
ooooooo
ooooooo
.....oo
oooo...
ooooooo"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """4
.oo.
..oo
o..o
oo.."""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """1
o"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """2
oo
.."""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例5(self):
        input = """2
o.
o."""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例6(self):
        input = """3
ooo
o..
o.."""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例7(self):
        input = """4
....
....
....
...."""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
