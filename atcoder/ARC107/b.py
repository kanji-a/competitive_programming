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
    N, K = LI()

    ans = 0
    # a+bを決める
    for i in range(2, 2 * N + 1):
        ab = i - 1 - 2 * max(i - 1 - N, 0)
        cd = max(i - K - 1 - 2 * max(i - K - 1 - N, 0), 0)
        # print(i, ab, cd)
        ans += ab * cd

    print(ans)

if __name__ == '__main__':
    resolve()
