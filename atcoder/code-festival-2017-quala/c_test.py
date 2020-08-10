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
        input = """3 4
aabb
aabb
aacc"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 2
aa
bb"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 1
t
w
e
e
t"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """2 5
abxba
abyba"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """1 1
z"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
