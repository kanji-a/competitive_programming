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
    c = SS()

    b = ('A', 'B', 'X', 'Y')
    bb = tuple([i + j for i, j in itertools.product(b, b)])

    ans = INF
    for i, j in itertools.product(bb, bb):
        if j != i:
            cnt = 0
            idx = 0
            while idx < N - 1:
                if c[idx] + c[idx+1] in (i, j):
                    idx += 2
                else:
                    idx += 1
                cnt += 1
            if idx == N - 1:
                cnt += 1
            ans = min(cnt, ans)

    print(ans)

if __name__ == '__main__':
    resolve()
