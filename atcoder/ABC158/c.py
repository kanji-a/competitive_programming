import sys
input = lambda: sys.stdin.readline().rstrip() 
import math

def resolve():
    A, B = map(int, input().split())
    aa_min = A / 0.08
    aa_max = (A+1) / 0.08
    bb_min = B / 0.1
    bb_max = (B+1) / 0.1
    if aa_min < bb_max and bb_min < aa_max:
        print(math.ceil(max(aa_min, bb_min)))
    else:
        print('-1')

if __name__ == '__main__':
    resolve()
