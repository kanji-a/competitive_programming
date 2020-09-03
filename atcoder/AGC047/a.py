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

    # 2と5を因数としていくつ含むか
    cnt = collections.Counter()
    for _ in range(N):
        A = SS()
        cnt2 = 0
        cnt5 = 0
        if '.' in A:
            idx = A.index('.')
            cnt2 -= len(A) - 1 - idx
            cnt5 -= len(A) - 1 - idx
            A = int(A[:idx] + A[idx+1:])
        else:
            A = int(A)
        while A % 2 == 0:
            A //= 2
            cnt2 += 1
        while A % 5 == 0:
            A //= 5
            cnt5 += 1
        cnt[(cnt2, cnt5)] += 1

    ans = 0
    for c0, c1 in itertools.combinations_with_replacement(cnt.items(), 2):
        k0, v0 = c0
        k1, v1 = c1
        if k0[0] + k1[0] >= 0 and k0[1] + k1[1] >= 0:
            if k0 == k1:
                ans += v0 * (v0 - 1) // 2
            else:
                ans += v0 * v1

    print(ans)

if __name__ == '__main__':
    resolve()
