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
    G = collections.defaultdict(list)
    for _ in range(N - 1):
        A, B = LI_()
        G[A].append(B)
        G[B].append(A)

    dist = [0] * N
    que = collections.deque()
    que.append(0)
    while que:
        c = que.popleft()
        for n in G[c]:
            if dist[n] == 0:
                que.append(n)
                dist[n] = dist[c] + 1

    ans_e = []
    ans_o = []
    for i, e in enumerate(dist):
        if e % 2 == 0:
            ans_e.append(i + 1)
        else:
            ans_o.append(i + 1)

    if len(ans_e) >= N // 2:
        print(*ans_e[:N//2])
    else:
        print(*ans_o[:N//2])
        
if __name__ == '__main__':
    resolve()
