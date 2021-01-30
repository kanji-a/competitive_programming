import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
INF = float('inf')
MOD = 10**9+7

# エラー出さないための定義
class DSU():
    def same(self, x, y):
        pass
    def merge(self, x, y):
        pass
class FenwickTree():
    def add(self, p, i):
        pass
    def sum(self, l, r):
        pass

# https://qiita.com/derodero24/items/91b6468e66923a87f39f#ユーザ定義型３評価-
# https://kadzus.hatenadiary.org/entry/20081211/1229023326
# 二項係数
def comb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = list(range(n - r + 1, n + 1))
    denominator = list(range(1, r + 1))

    for p in range(2, r + 1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p - 1, r, p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot
    
    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result

# 二項係数を素数で割った余り
def combMod(n, r, p):
    numer = 1
    denom = 1
    for i in range(1, r+1):
        numer = numer * (n-r+i) % p
        denom = denom * i % p
    return numer * pow(denom, p-2, p) % p

# conbMod0に使うfactとfactinvを求める
def factorialMod(n, p):
    fact = [0] * (n+1)
    fact[0] = fact[1] = 1
    factinv = [0] * (n+1)
    factinv[0] = factinv[1] = 1
    inv = [0] * (n+1)
    inv[1] = 1
    for i in range(2, n + 1):
        fact[i] = (fact[i-1] * i) % p
        inv[i] = (-inv[p % i] * (p // i)) % p
        factinv[i] = (factinv[i-1] * inv[i]) % p
    return fact, factinv

# 二項係数を素数で割った余り 繰り返し求める場合はこっち
def combMod0(n, r, fact, factinv, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

def is_prime(n):
    if n==0 or n==1: return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

# エラトステネスの篩
def sieve(n):
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*2, n+1, i):
                is_prime[j] = False
    return [i for i in range(n+1) if is_prime[i]]

# 素数リストがある場合の素因数分解
def primeFactorization(n, primes):
    ans = []
    temp = n
    for p in primes:
        while temp%p == 0:
            ans.append(p)
            temp //= p
    if temp > 1:
        ans.append(temp)
    return collections.Counter(ans)

# 素数リストがない場合の素因数分解 基本これがベスト
def primeFactorization1(n):
    ans = []
    temp = n
    while temp%2 == 0:
        ans.append(2)
        temp //= 2
    for i in range(3, int(n**0.5)+1, 2):
        while temp%i == 0:
            ans.append(i)
            temp //= i
    if temp > 1:
        ans.append(temp)
    return collections.Counter(ans)

# 複数の数を高速で素因数分解
def primeFactorization2(n):
    D = list(range(n + 1))
    for i in range(2, int(n ** 0.5) + 1):
        if D[i] == i:
            for j in range(i, n + 1, i):
                if D[j] == j:
                    D[j] = i
    return D

# 使用例
# D = primeFactorization2(n)
# for i in A:
#     tmp = i
#     cnt = collections.Counter()
#     while tmp != 1:
#         cnt[D[tmp]] += 1
#         tmp //= D[tmp]


class WeightedUnionFind():
    def __init__(self, n):
        self.n = n
        self.par = list(range(n))
        self.rank = [0] * n
        self.diff_weight = [0] * n

    def root(self, x):
        if self.par[x] == x:
            return x
        else:
            r = self.root(self.par[x])
            self.diff_weight[x] += self.diff_weight[self.par[x]]
            self.par[x] = r
            return r

    def issame(self, x, y):
        return self.root(x) == self.root(y)

    def merge(self, x, y, w):
        w += self.weight(x)
        w -= self.weight(y)
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.rank[x] < self.rank[y]:
            x, y = y, x
            w = -w
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        self.par[y] = x
        self.diff_weight[y] = w
        return True

    def weight(self, x):
        self.root(x)
        return self.diff_weight[x]

    def diff(self, x, y):
        return self.weight(y) - self.weight(x)

def is_ok(x):
    pass
def binsearch(a, x):
    ng = 10 ** 9
    ok = 0
    while abs(ok - ng) > 10e-7:
        m = (ng + ok) / 2
        if is_ok(m):
            ok = m
        else:
            ng = m
    return ok

def dijkstra(G, N, s):
    que = []
    d = [INF] * N
    d[s] = 0
    heapq.heappush(que, (d[s], s))

    while que:
        p = heapq.heappop(que)
        v = p[1]
        if d[v] < p[0]: continue
        for e in G[v]:
            if d[e[0]] > d[v] + e[1]:
                d[e[0]] = d[v] + e[1]
                heapq.heappush(que, (d[e[0]], e[0]))
    return d

def warshall_floyd(d):
    V = len(d)
    for i in range(V):
        d[i][i] = 0
    for k in range(V):
        for i in range(V):
            for j in range(V):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

def kruskal(es, V):
    es.sort(key=lambda x:x[2])
    dsu = DSU(V)
    res = 0
    for e in es:
        if not dsu.same(e[0], e[1]):
            dsu.merge(e[0], e[1])
            res += e[2]
    return res

def lis(a):
    dp = [INF]*len(a)
    for i in a:
        dp[bisect.bisect_left(dp, i)] = i
    return bisect.bisect_left(dp, INF)

# listを分割 is_ng(x)は分割条件
# ex. 増加列だったらa[i] > a[i+1]
# 未試用のためバグあるかも
def is_ng(x):
    pass
def split_list(a):
    ret = []
    tmp = []
    l = len(a)
    for i in range(l):
        tmp.append(a[i])
        if i < l - 1 and is_ng(i) or i == l - 1:
            ret.append(tmp)
            tmp = []
    return ret

# 行列乗算MOD
def matMulMod(A, B):
    A_h = len(A)
    B_h = len(B)
    B_w = len(B[0])
    C = [[0] * B_w for _ in range(A_h)]
    for i in range(A_h):
        for j in range(B_w):
            for k in range(B_h):
                C[i][j] += A[i][k] * B[k][j]
                C[i][j] %= MOD
    return C

# 行列累乗MOD
def matPowMod(A, n):
    s = len(A)
    B = [[int(i == j) for j in range(s)] for i in range(s)]
    while n > 0:
        if n & 1:
            B = matMulMod(B, A)
        A = matMulMod(A, A)
        n >>= 1
    return B
    
# 繰り返し2乗法 powはmod指定しないと遅い
def my_pow(x, y):
    res = 1
    while y:
        if y & 1:
            res *= x
        x **= 2
        y >>= 1
    return res

def inversion_number(n, A):
    sorted_A = sorted(A)
    d = {}
    for i, e in enumerate(sorted_A):
        d[e] = i

    fwt = FenwickTree(n)
    ans = 0
    for i, e in enumerate(A):
        fwt.add(d[e], 1)
        ans += i - fwt.sum(0, d[e])
    return ans

# 以下、ACLにあるのでいらなくなったもの

# class Bit:
#     def __init__(self, n):
#         self.size = n
#         self.tree = [0] * (n + 1)

#     def sum(self, i):
#         s = 0
#         while i > 0:
#             s += self.tree[i]
#             i -= i & -i
#         return s

#     def add(self, i, x):
#         while i <= self.size:
#             self.tree[i] += x
#             i += i & -i

# RMQ用のセグメント木
# queryの呼び出し: query(a, b, 0, 0, st.n)
# class segmentTree():
#     def __init__(self, n_):
#         self.n = 1
#         self.int_max = 2 ** 31 - 1
#         while self.n < n_:
#             self.n *= 2
#         self.dat = [self.int_max] * (2 * self.n - 1)

#     def update(self, k, a):
#         k += self.n - 1
#         self.dat[k] = a
#         while k > 0:
#             k = (k - 1) // 2
#             self.dat[k] = min(self.dat[k * 2 + 1], self.dat[k * 2 + 2])

#     def query(self, a, b, k, l, r):
#         if r <= a or b <= l:
#             return self.int_max
#         if a <= l and r <= b:
#             return self.dat[k]
#         else:
#             vl = self.query(a, b, k * 2 + 1, l, (l + r) // 2)
#             vr = self.query(a, b, k * 2 + 2, (l + r) // 2, r)
#             return min(vl, vr)
        
# drken
# class UnionFind():
#     def __init__(self, n):
#         self.n = n
#         self.par = list(range(n))
#         self.rank = [0] * n

#     def root(self, x):
#         if self.par[x] == x:
#             return x
#         else:
#             r = self.root(self.par[x])
#             self.par[x] = r
#             return r

#     def issame(self, x, y):
#         return self.root(x) == self.root(y)

#     def merge(self, x, y):
#         x = self.root(x)
#         y = self.root(y)
#         if x == y:
#             return False
#         if self.rank[x] < self.rank[y]:
#             x, y = y, x
#         if self.rank[x] == self.rank[y]:
#             self.rank[x] += 1
#         self.par[y] = x
#         return True

# note.nkmk
# class UnionFind():
#     def __init__(self, n):
#         self.n = n
#         self.parents = [-1] * n

#     def find(self, x):
#         if self.parents[x] < 0:
#             return x
#         else:
#             self.parents[x] = self.find(self.parents[x])
#             return self.parents[x]

#     def unite(self, x, y):
#         x = self.find(x)
#         y = self.find(y)

#         if x == y:
#             return

#         if self.parents[x] > self.parents[y]:
#             x, y = y, x

#         self.parents[x] += self.parents[y]
#         self.parents[y] = x

#     def same(self, x, y):
#         return self.find(x) == self.find(y)

#     def size(self, x):
#         return -self.parents[self.find(x)]

#     def members(self, x):
#         root = self.find(x)
#         return [i for i in range(self.n) if self.find(i) == root]

#     def roots(self):
#         return [i for i, x in enumerate(self.parents) if x < 0]

#     def group_count(self):
#         return len(self.roots())

#     def all_group_members(self):
#         return {r: self.members(r) for r in self.roots()}

#     def __str__(self):
#         return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())