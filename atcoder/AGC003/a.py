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

    cnt = collections.Counter(S)
    n = cnt['N']
    w = cnt['W']
    s = cnt['S']
    e = cnt['E']
    if (n > 0 and s > 0 or n == s == 0) and (w > 0 and e > 0 or w == e == 0):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    resolve()
