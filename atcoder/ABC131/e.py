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

    # Kの上界として、全ての頂点対の数がある。
    # グラフが連結なので頂点数-1個の頂点対は最短距離1になる。
    # よってKの最大値はNC2-(N-1)
    max_K = N * (N - 1) // 2 - (N - 1)
    if K <= max_K:
        # Kが最大値を取るのはスター型
        # そこから葉同士をくっつけて減らしていく
        print((N - 1) + max_K - K)
        for i in range(1, N):
            print(i, N)
        cnt = max_K
        for i, j in itertools.combinations(range(1, N), 2):
            if cnt == K:
                break
            print(i, j)
            cnt -= 1
    else:
        print(-1)

if __name__ == '__main__':
    resolve()
