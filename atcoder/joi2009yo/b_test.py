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
        input = """23
23
20
15
15
14
13
9
7
6
25
19
17
17
16
13
12
11
9
5"""
        output = """66 61"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """17
25
23
25
79
29
1
61
59
100
44
74
94
57
13
54
82
0
42
45"""
        output = """240 250"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()