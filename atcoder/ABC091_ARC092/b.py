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
    s = [SS() for _ in range(N)]
    M = I()
    t = [SS() for _ in range(M)]

    cnt_s = collections.Counter(s)
    cnt_t = collections.Counter(t)
    ans = max([max(cnt_s[i] - cnt_t[i], 0) for i in (cnt_s.keys() | cnt_t.keys())])
    print(ans)

if __name__ == '__main__':
    resolve()
