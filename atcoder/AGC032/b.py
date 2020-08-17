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

    # Nが偶数の場合、完全N//2-partiteグラフ
    # Nが奇数の場合、完全(N-1)//2-partiteグラフに全ての頂点と隣接している頂点Nを加えたもの
    ans = []

    def f(n):
        for i in range(1, n // 2 + 1):
            for j in range(1, n + 1):
                if j != i and j != n + 1 - i:
                    if j < i:
                        ans.append((j, i))
                    else:
                        ans.append((i, j))
                    if j < n + 1 - i:
                        ans.append((j, n + 1 - i))
                    else:
                        ans.append((n + 1 - i, j))

    if N % 2 == 0:
        f(N)
    else:
        if N >= 5:
            f(N - 1)
        for i in range(1, N):
            ans.append((i, N))

    ans = set(ans)
    print(len(ans))
    for i, j in ans:
        print(i, j)
        
if __name__ == '__main__':
    resolve()
