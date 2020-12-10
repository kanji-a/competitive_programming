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
    N, M = LI()
    xyz = [LI() for _ in range(N)]

    # 絶対値が無ければ3つの総和が大きいものから選べば良い
    # 要素ごとに符号をそのまま足すか反転して足すか全パターン試す
    ans = 0
    for i in range(2 ** 3):
        tmp = [0] * N
        for j in range(3):
            s = 1 if i >> j & 1 else -1
            tmp = [tmp[i] + s * xyz[i][j] for i in range(N)]
        tmp.sort(reverse=True)
        ans = max(sum(tmp[:M]), ans)

    print(ans)

if __name__ == '__main__':
    resolve()
