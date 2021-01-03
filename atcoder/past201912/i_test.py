from i import resolve
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
YYY 100
YYN 20
YNY 10
NYY 25"""
        output = """30"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 4
YNNNN 10
NYNNN 10
NNYNN 10
NNNYN 10"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 14
YNNYNNNYYN 774472905
YYNNNNNYYY 75967554
NNNNNNNNNN 829389188
NNNNYYNNNN 157257407
YNNYNNYNNN 233604939
NYYNNNNNYY 40099278
NNNNYNNNNN 599672237
NNNYNNNNYY 511018842
NNNYNNYNYN 883299962
NNNNNNNNYN 883093359
NNNNNYNYNY 54742561
NYNNYYYNNY 386272705
NNNNYYNNNN 565075143
NNYNYNNNYN 123300589"""
        output = """451747367"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
