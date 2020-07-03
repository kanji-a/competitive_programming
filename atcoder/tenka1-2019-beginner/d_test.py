from d import resolve
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
1
1
1
2"""
        output = """18"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
1
3
2
3
5
2"""
        output = """150"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """20
3
1
4
1
5
9
2
6
5
3
5
8
9
7
9
3
2
3
8
4"""
        output = """563038556"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
