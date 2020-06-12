import sys
input = lambda: sys.stdin.readline().rstrip() 
import math

def resolve():
    L = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())

    print(L-max(math.ceil(A/C), math.ceil(B/D)))

if __name__ == '__main__':
    resolve()