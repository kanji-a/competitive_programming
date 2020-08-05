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
    N, K = LI()

    # 愚直なやり方で見つけたパターンをb毎の式に落とす
    # for a in range(1, N+1):
    #     print([a % b for b in range(1, N+1)])

    ans = 0
    for b in range(K + 1, N + 1):
        # 繰り返し分
        ans += (b - K) * (N // b)
        # 半端分
        ans += max(N % b - max(K - 1, 0), 0)

    print(ans)

if __name__ == '__main__':
    resolve()
