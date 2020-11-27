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

class segmentTree():
    def __init__(self, n_):
        self.n = 1
        self.int_min = 0
        while self.n < n_:
            self.n *= 2
        self.dat = [self.int_min] * (2 * self.n - 1)

    def update(self, k, a):
        k += self.n - 1
        self.dat[k] = a
        while k > 0:
            k = (k - 1) // 2
            self.dat[k] = max(self.dat[k * 2 + 1], self.dat[k * 2 + 2])

    def query(self, a, b, k, l, r):
        if r <= a or b <= l:
            return self.int_min
        if a <= l and r <= b:
            return self.dat[k]
        else:
            vl = self.query(a, b, k * 2 + 1, l, (l + r) // 2)
            vr = self.query(a, b, k * 2 + 2, (l + r) // 2, r)
            return max(vl, vr)

def resolve():
    n = I()
    slp = [LI() for _ in range(n)]
    m = I()
    w = [I() for _ in range(m)]
    max_w = max(w)

    dp = segmentTree(max_w + 1)
    for i in range(1, max_w + 1):
        for s, l, p in slp:
            # for j in range(s, l + 1):
            #     if i - j >= 0:
            #         dp[i] = max(dp[i-j] + p, dp[i])
            if i - s >= 0:
                tmp = dp.query(max(i - l, 0), i - s + 1, 0, 0, dp.n)
                if tmp + p > dp.dat[dp.n-1+i]:
                    dp.update(i, tmp + p)

    ans = [dp.dat[dp.n-1+i] for i in w]
    if 0 in ans:
        print(-1)
    else:
        for i in ans:
            print(i)

if __name__ == '__main__':
    resolve()