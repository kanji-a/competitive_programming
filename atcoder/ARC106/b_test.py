from b import resolve
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
        input = """3 2
1 2 3
2 2 2
1 2
2 3"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 0
5
5"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 1
1 1
2 1
1 2"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """17 9
-905371741 -999219903 969314057 -989982132 -87720225 -175700172 -993990465 929461728 895449935 -999016241 782467448 -906404298 578539175 9684413 -619191091 -952046546 125053320
-440503430 -997661446 -912471383 -995879434 932992245 -928388880 -616761933 929461728 210953513 -994677396 648190629 -530944122 578539175 9684413 595786809 -952046546 125053320
2 10
6 12
9 11
11 5
7 6
3 15
3 1
1 9
10 4"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
