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
    N, K = LI()
    a = LI()
    max_a = max(a)

    cnt = collections.Counter(a)
    ans = 0
    num = K
    for i in range(max_a + 2):
        if cnt[i] < num:
            ans += i * (num - cnt[i])
            num = cnt[i]

    print(ans)

if __name__ == '__main__':
    resolve()
