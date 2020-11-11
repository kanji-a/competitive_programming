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
    N = SS()

    cnt = collections.Counter([int(i) % 3 for i in N])
    # print(cnt)
    ans = abs(cnt[1] - cnt[2]) % 3
    if ans == len(N):
        print(-1)
    elif ans != 0:
        if cnt[1] < cnt[2] and cnt[1] >= 1 and ans == 2 or cnt[1] > cnt[2] and cnt[2] >= 1 and ans == 2:
            ans = 1
        print(ans)
    else:
        print(ans)

if __name__ == '__main__':
    resolve()
