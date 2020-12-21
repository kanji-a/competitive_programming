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
        input = """4
10 4 3
1000 11 2
998244353 897581057 595591169
10000 6 14"""
        output = """2
-1
249561088
3571"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
