import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
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
    S = SS()

    # 各アルファベットに対して、どこか1個以下使うパターンがある
    ans = 1
    cnt = collections.Counter(S)
    for i in cnt.values():
        ans *= (i + 1)
        ans %= MOD
    ans -= 1

    print(ans)

if __name__ == '__main__':
    resolve()
