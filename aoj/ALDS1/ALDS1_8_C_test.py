from ALDS1_8_C import resolve
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
        input = """18
insert 8
insert 2
insert 3
insert 7
insert 22
insert 1
find 1
find 2
find 3
find 4
find 5
find 6
find 7
find 8
print
delete 3
delete 7
print"""
        output = """yes
yes
yes
no
no
no
yes
yes
 1 2 3 7 8 22
 8 2 1 3 7 22
 1 2 8 22
 8 2 1 22"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """43
insert 30
insert 17
insert 88
insert 53
insert 5
insert 20
insert 18
insert 28
insert 27
insert 60
print
find -1
find 2
find 3
find 4
find 5
find 6
find 10
find 17
find 28
find 29
find 30
find 31
find 50
find 51
find 52
find 53
find 54
find 60
find 88
find 89
insert 2000000000
insert 55
insert 63
insert -1
insert 8
print
delete 53
delete 2000000000
delete 20
delete 5
delete 8
print"""
        output = """ 5 17 18 20 27 28 30 53 60 88
 30 17 5 20 18 28 27 88 53 60
no
no
no
no
yes
no
no
yes
yes
no
yes
no
no
no
no
yes
no
yes
yes
no
 -1 5 8 17 18 20 27 28 30 53 55 60 63 88 2000000000
 30 17 5 -1 8 20 18 28 27 88 53 60 55 63 2000000000
 -1 17 18 27 28 30 55 60 63 88
 30 17 -1 27 18 28 88 60 55 63"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()