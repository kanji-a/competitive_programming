from f import resolve
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
        input = """3 8
1 3 1 10
0 2 3
1 2 3 20
1 1 2 5
0 3 2
1 1 3 7
1 2 1 9
0 2 3"""
        output = """-1
15
12"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """5 16
1 1 2 343750
1 1 3 3343
1 1 4 347392
1 1 5 5497
1 2 3 123394
1 2 4 545492
1 2 5 458
1 3 4 343983
1 3 5 843468
1 4 5 15934
0 2 1
0 4 1
0 3 2
0 4 2
0 4 3
0 5 3"""
        output = """5955
21431
9298
16392
24774
8840"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()