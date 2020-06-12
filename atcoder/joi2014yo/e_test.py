from e import resolve
import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    maxDiff = None
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """6 6
400 2
200 1
600 3
1000 1
300 5
700 4
1 2
2 3
3 6
4 6
1 5
2 4"""
        output = """700"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()