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
    def test_入力例1(self):
        input = """4 3
5 3 1 2
3 2 4"""
        output = """264"""
        self.assertIO(input, output)
    def test_入力例2(self):
        input = """3 2
23 12 9
2 3"""
        output = """876796540"""
        self.assertIO(input, output)
    def test_入力例3(self):
        input = """2 1
1000000000 1000000000
2"""
        output = """625113690"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()