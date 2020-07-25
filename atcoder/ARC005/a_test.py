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

    def test_入力例_1(self):
        input = """5
Takahashikun is not an eel."""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
TAKAHASHIKUN loves TAKAHASHIKUN and takahashikun."""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
He is not takahasikun but Takahashikun."""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1
takahashikunTAKAHASHIKUNtakahashikun."""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """18
You should give Kabayaki to Takahashikun on July twenty seventh if you suspect that he is an eel."""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
