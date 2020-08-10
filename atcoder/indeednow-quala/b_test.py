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

    def test_入力例1(self):
        input = """10
nowindeed
indeedwow
windoneed
indeednow
wondeedni
a
indonow
ddeennoiw
indeednoww
indeow"""
        output = """YES
NO
YES
YES
YES
NO
NO
YES
NO
NO"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
