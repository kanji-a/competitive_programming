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
    N = I()

    ng = 0
    ok = N
    print(ng, flush=True)
    ng_s = SS()
    ok_s = ng_s
    while abs(ok-ng)>1:
        m = (ng+ok)//2
        print(m, flush=True)
        s = SS()
        if s == 'Vacant':
            sys.exit()
        elif (ok - m) % 2 == 1 and ok_s != s or (ok - m) % 2 == 0 and ok_s == s:
            ok = m
            ok_s = s
        else:
            ng = m
            ng_s = s

if __name__ == '__main__':
    resolve()
