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

    def query(self, k):
        k += self.n - 1
        res = self.dat[k]
        while k > 0:
            k = (k - 1) // 2
            res += self.dat[k]
        return res

    def update(self, a, b, k, l, r, x):
        if r <= a or b <= l:
            return
        if a <= l and r <= b:
            self.dat[k] += x
        else:
            self.update(a, b, k * 2 + 1, l, (l + r) // 2, x)
            self.update(a, b, k * 2 + 2, (l + r) // 2, r, x)
        
def resolve():
    n, q = LI()
    st = segmentTree(n)
    for _ in range(q):
        query = LI()
        if query[0] == 0:
            s, t, x = query[1:]
            st.update(s - 1, t, 0, 0, st.n, x)
        else:
            i = query[1]
            ans = st.query(i - 1)
            print(ans)

if __name__ == '__main__':
    resolve()
