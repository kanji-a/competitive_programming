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
    S = list(SS())
    T = list(SS())

    cnt_S = S.count('0')
    cnt_T = T.count('0')
    # print(cnt_S, cnt_T)

    # 1の数が一致していることが可能どうかの必要十分条件
    if cnt_S != cnt_T:
        print(-1)
        return
    if S == T:
        print(0) 
        return

    idx_0_S = collections.deque()
    idx_0_T = collections.deque()
    for i in range(N):
        if S[i] == '0':
            idx_0_S.append(i)
        if T[i] == '0':
            idx_0_T.append(i)
    # print(idx_0_S)
    # print(idx_0_T)

    ans = 0
    for i in range(N):
        if idx_0_S:
            if idx_0_S[0] != idx_0_T[0]:
                ans += 1
            idx_0_S.popleft()
            idx_0_T.popleft()

    
    print(ans)

if __name__ == '__main__':
    resolve()
