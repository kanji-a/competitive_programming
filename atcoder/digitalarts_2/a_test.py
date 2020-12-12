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
        input = """abc aaa ababa abcba abc
2
abc
**a**"""
        output = """*** aaa ***** abcba ***"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """aaaa aaa aaaaaa aaaa
3
a
aa
aaa"""
        output = """aaaa *** aaaaaa aaaa"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """i have a pen
1
*"""
        output = """* have * pen"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """digital arts
1
digital*arts"""
        output = """digital arts"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
