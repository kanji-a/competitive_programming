from d import resolve
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
        input = """4
1148-1210
1323-1401
1106-1123
1129-1203"""
        output = """1105-1210
1320-1405"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1
0000-2400"""
        output = """0000-2400"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
1157-1306
1159-1307
1158-1259
1230-1240
1157-1306
1315-1317"""
        output = """1155-1310
1315-1320"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
