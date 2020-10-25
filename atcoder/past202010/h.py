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
    N, M, K = LI()
    s = [[int(i) for i in SS()] for _ in range(N)]

    ans = 0
    # 正方形の左上
    for i, j in itertools.product(range(N), range(M)):
        # 正方形の辺の長さ
        for k in range(1, min(N - i, M - j) + 1):
            cnt = [0] * 10
            for l, m in itertools.product(range(k), repeat=2):
                cnt[s[i+l][j+m]] += 1
            for l in range(10):
                if k ** 2 - cnt[l] <= K:
                    ans = max(k, ans)

    print(ans)

if __name__ == '__main__':
    resolve()
