from k import resolve
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
        input = """7
-1
1
1
2
2
3
3
6
7 1
4 1
2 3
5 1
5 2
2 5"""
        output = """Yes
Yes
No
Yes
Yes
No"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """20
4
11
12
-1
1
13
13
4
6
20
1
1
20
10
8
8
20
10
18
1
20
18 14
11 3
2 13
13 11
10 15
9 5
17 11
18 10
1 16
9 4
19 6
5 10
17 8
15 8
5 16
6 20
3 19
10 12
5 13
18 1"""
        output = """No
No
No
No
No
No
No
Yes
No
Yes
No
No
No
Yes
No
Yes
No
No
No
Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
