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
        self.int_max = 2 ** 31 - 1
        while self.n < n_:
            self.n *= 2
        self.dat = [self.int_max] * (2 * self.n - 1)

    def update(self, k, a):
        k += self.n - 1
        self.dat[k] = a
        while k > 0:
            k = (k - 1) // 2
            self.dat[k] = min(self.dat[k * 2 + 1], self.dat[k * 2 + 2])

    def query(self, a, b, k, l, r):
        if r <= a or b <= l:
            return self.int_max
        if a <= l and r <= b:
            return self.dat[k]
        else:
            vl = self.query(a, b, k * 2 + 1, l, (l + r) // 2)
            vr = self.query(a, b, k * 2 + 2, (l + r) // 2, r)
            return min(vl, vr)
        
def resolve():
    n, q = LI()
    st = segmentTree(n)
    for _ in range(q):
        com, x, y = LI()
        if com == 0:
            st.update(x, y)
        else:
            ans = st.query(x, y + 1, 0, 0, st.n)
            print(ans)

if __name__ == '__main__':
    resolve()
