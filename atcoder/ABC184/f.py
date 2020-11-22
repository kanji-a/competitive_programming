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
    N, T = LI()
    A = LI()
    A_f = N // 2
    A_b = N - A_f

    s_f = []
    for i in range(2 ** A_f):
        s = 0
        for j in range(A_f):
            if i >> j & 1:
                s += A[j]
        s_f.append(s)
    s_b = []
    for i in range(2 ** A_b):
        s = 0
        for j in range(A_b):
            if i >> j & 1:
                s += A[A_f+j]
        s_b.append(s)
    s_b.sort()

    # print(s_f)
    # print(s_b)
    ans = 0
    for i in s_f:
        idx = bisect.bisect_right(s_b, T - i)
        if 0 <= idx - 1 < len(s_b):
            # print(i, idx, s_b[idx - 1])
            ans = max(i + s_b[idx - 1], ans)

    print(ans)

if __name__ == '__main__':
    resolve()
