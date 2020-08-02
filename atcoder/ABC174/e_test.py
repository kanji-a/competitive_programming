from e import resolve
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
        input = """2 3
7 9"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 0
3 4 5"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 10
158260522 877914575 602436426 24979445 861648772 623690081 433933447 476190629 262703497 211047202"""
        output = """292638192"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
