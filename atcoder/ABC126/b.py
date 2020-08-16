import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    S = SS()

    f = int(S[:2])
    b = int(S[2:])
    if 1 <= f <= 12 and 1 <= b <= 12:
        print('AMBIGUOUS')
    elif 1 <= b <= 12:
        print('YYMM')
    elif 1 <= f <= 12:
        print('MMYY')
    else:
        print('NA')

if __name__ == '__main__':
    resolve()
