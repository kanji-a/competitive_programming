from o import resolve
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
        input = """3 3
1 2 2
2 3 5
3 1 3"""
        output = """5
7
5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 7
1 2 8
2 3 9
2 4 7
3 1 5
3 4 6
4 1 8
3 5 1"""
        output = """20
21
19
19
19
21
19"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8 10
1 2 314159265
2 3 358979323
3 4 846264338
1 3 327950288
1 4 419716939
2 4 937510582
1 5 97494459
1 6 230781640
1 7 628620899
1 8 862803482"""
        output = """2881526972
2912556007
3308074371
2881526972
2881526972
3399320615
2881526972
2881526972
2881526972
2881526972"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
