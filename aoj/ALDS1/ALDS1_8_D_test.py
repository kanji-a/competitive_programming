from ALDS1_8_D import resolve
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
        input = """16
insert 35 99
insert 3 80
insert 1 53
insert 14 25
insert 80 76
insert 42 3
insert 86 47
insert 21 12
insert 7 10
insert 6 90
print
find 21
find 22
delete 35
delete 99
print"""
        output = """ 1 3 6 7 14 21 35 42 80 86
 35 6 3 1 14 7 21 80 42 86
yes
no
 1 3 6 7 14 21 42 80 86
 6 3 1 80 14 7 21 42 86"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()