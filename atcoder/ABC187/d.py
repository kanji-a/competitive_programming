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
    N = I()
    AB = [LI() for _ in range(N)]
    aoki = sum([i[0] for i in AB])
    # print(aoki)
    AB_= sorted([2 * i + j for i, j in AB], reverse=True)
    # print(AB_)
    ans = 0
    s = 0
    for i in range(N):
        s += AB_[i]
        if s > aoki:
            ans = i + 1
            break

    print(ans)

if __name__ == '__main__':
    resolve()
