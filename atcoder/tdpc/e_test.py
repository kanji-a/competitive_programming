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

    def test_Sample_Input_1(self):
        input = """3
100"""
        output = """33"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """7
123456789012345678901234567890"""
        output = """468357804"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
