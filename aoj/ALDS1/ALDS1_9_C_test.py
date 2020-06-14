from ALDS1_9_C import resolve
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
        input = """insert 8
insert 2
extract
insert 10
extract
insert 11
extract
extract
end"""
        output = """8
10
11
2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()