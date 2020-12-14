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
        while self.n < n_:
            self.n *= 2
        self.dat = [0] * (2 * self.n - 1)

    def update(self, k, a):
        k += self.n - 1
        self.dat[k] ^= a
        while k > 0:
            k = (k - 1) // 2
            self.dat[k] = self.dat[k * 2 + 1] ^ self.dat[k * 2 + 2]

    def query(self, a, b, k, l, r):
        if r <= a or b <= l:
            return 0
        if a <= l and r <= b:
            return self.dat[k]
        else:
            vl = self.query(a, b, k * 2 + 1, l, (l + r) // 2)
            vr = self.query(a, b, k * 2 + 2, (l + r) // 2, r)
            return vl ^ vr

def resolve():
    N, Q = LI()
    A = LI()
    st = segmentTree(N)
    for i in range(N):
        st.update(i, A[i])
    # print(st.dat)

    for _ in range(Q):
        T, X, Y = LI()
        if T == 1:
            st.update(X - 1, Y)
        else:
            ans = st.query(X - 1, Y, 0, 0, st.n)
            print(ans)

if __name__ == '__main__':
    resolve()
