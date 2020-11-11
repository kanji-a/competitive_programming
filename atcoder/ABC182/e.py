import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 10**9+7
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    H, W, N, M = LI()
    AB = [LI_() for _ in range(N)]
    S = [['.'] * W for _ in range(H)]
    for _ in range(M):
        C, D = LI_()
        S[C][D] = '#'

    for i in S:
        print(i)

    left = [[0] * W for _ in range(H)]
    for i in range(H):
        cnt = 0
        for j in range(W):
            if S[i][j] == '.':
                cnt += 1
                left[i][j] = cnt
            else:
                cnt = 0

    for i in left:
        print(i)

if __name__ == '__main__':
    resolve()
