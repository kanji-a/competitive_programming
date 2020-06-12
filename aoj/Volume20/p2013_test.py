from p2013 import resolve
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
        input = """3
05:47:15 09:54:40
12:12:59 12:13:00
16:30:20 21:18:53
6
00:00:00 03:00:00
01:00:00 03:00:00
02:00:00 03:00:00
03:00:00 04:00:00
03:00:00 05:00:00
03:00:00 06:00:00
0"""
        output = """1
3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()