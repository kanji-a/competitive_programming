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
    T = I()

    d = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}

    cx = cy = 0
    cnt = 0
    for i in S:
        if i == '?':
            cnt += 1
        else:
            cx += d[i][0]
            cy += d[i][1]

    if T == 1:
        print(abs(cx) + abs(cy) + cnt)
    else:
        d_m_q = abs(cx) + abs(cy) - cnt
        if d_m_q >= 0:
            print(d_m_q)
        else:
            print(-d_m_q % 2)

if __name__ == '__main__':
    resolve()
