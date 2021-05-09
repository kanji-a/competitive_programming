#!/usr/bin/env python3
import bisect, collections, copy, functools, heapq, itertools, math, operator, string, sys, typing
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)
INF = float('inf')
MOD = 10 ** 9 + 7
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N = I()
    XY = [LF()for _ in range(N)]

    ans = 0
    # まずPjを固定する
    for j in range(N):
        # Pjを中心に点Pの偏角を求めてソート
        a = sorted(math.atan2(XY[i][1] - XY[j][1], XY[i][0] - XY[j][0]) * 180 / math.pi for i in range(N) if i != j)
        # print(a)
        for Pi_deg in a:
            if Pi_deg >= 180:
                continue
            idx = bisect.bisect_left(a, Pi_deg + 180)
            if idx < len(a):
                ans = max(min(a[idx] - Pi_deg, 360 - a[idx] + Pi_deg), ans)
            if 0 <= idx - 1:
                ans = max(min(a[idx-1] - Pi_deg, 360 - a[idx-1] + Pi_deg), ans)

    print(ans)

if __name__ == '__main__':
    resolve()
