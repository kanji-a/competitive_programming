from b import resolve
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
        input = """3 5 R
790319030
091076399
143245946
590051196
398226115
442567154
112705290
716433235
221041645"""
        output = """8226"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8 9 LU
206932999
471100777
973172688
108989704
246954192
399039569
944715218
003664867
219006823"""
        output = """2853"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 7 D
271573743
915078603
102553534
996473623
595593497
573572507
340348994
253066837
643845096"""
        output = """4646"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """2 2 LU
729142134
509607882
640003027
215270061
214055727
745319402
777708131
018697986
277156993"""
        output = """0700"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """8 7 RD
985877833
469488482
218647263
856777094
012249580
845463670
919136580
011130808
874387671"""
        output = """8878"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
