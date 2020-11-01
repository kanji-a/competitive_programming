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
        input = """5 3
1 2 3 4 7
1 3 8"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 7
31 60 84 23 16 13 32
96 80 73 76 87 57 29"""
        output = """34"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """15 10
554 525 541 814 661 279 668 360 382 175 833 783 688 793 736
496 732 455 306 189 207 976 73 567 759"""
        output = """239"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """7 2
31 60 84 23 16 13 32
20 25"""
        output = """30"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
