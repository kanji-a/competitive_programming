import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
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
    AB = [LI() for _ in range(M)]
    K = I()
    CD = [LI() for _ in range(K)]

    ans = 0
    for i in range(2 ** K):
        tmp = 0
        cnt = collections.Counter()
        for j in range(K):
            if i >> j & 1:
                cnt[CD[j][1]] += 1
            else:
                cnt[CD[j][0]] += 1
        for A, B in AB:
            if cnt[A] >= 1 and cnt[B] >= 1:
                tmp += 1
        ans = max(tmp, ans)

    print(ans)

if __name__ == '__main__':
    resolve()
