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
        input = """4 3
3 3 -4 -2"""
        output = """-6"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """10 40
5 4 3 2 -1 0 0 0 0 0"""
        output = """6"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """30 413
-170202098 -268409015 537203564 983211703 21608710 -443999067 -937727165 -97596546 -372334013 398994917 -972141167 798607104 -949068442 -959948616 37909651 0 886627544 -20098238 0 -948955241 0 -214720580 277222296 -18897162 834475626 0 -425610555 110117526 663621752 0"""
        output = """448283280358331064"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()