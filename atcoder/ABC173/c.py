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
    H, W, K = LI()
    c = [list(SS()) for _ in range(H)]

    ans = 0
    for i in range(2 ** H):
        for j in range(2 ** W):
            cnt = 0
            for k in range(H):
                for l in range(W):
                    if not ((i >> k & 1) or (j >> l & 1)):
                        if c[k][l] == '#':
                            cnt += 1
            if cnt == K:
                ans += 1

    print(ans)

if __name__ == '__main__':
    resolve()
