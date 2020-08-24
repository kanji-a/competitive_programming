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
def primeFactorization(n):
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

# テーブルを使う素因数分解 出力がおかしい
def primeFactorizationFromTable(n):
    # 最小素因数で分解
    product = [[1, i] for i in range(n+1)]
    for i in range(2, int(n**0.5)+1):
        # 合成数では割らない
        if product[i][0] == 1:
            # i**2より前は既に別の数で割られている
            for j in range(i**2, n+1, i):
                # 割られていない数のみ割る
                if product[j][0] == 1:
                    product[j][0] = i
                    product[j][1] = j // i
    # 表を辿って素因数分解を求める
    ans = []
    temp = n
    while product[temp][0] != 1:
        ans.append(product[temp][0])
        temp = product[temp][1]
        ans.append(product[temp][1])
    return ans

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.parents[self.find(x)]

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

def binsearch_left(a, x):
    ng = -1
    ok = len(a)
    while abs(ok-ng)>1:
        m = (ng+ok)//2
        if x<=a[m]:
            ok = m
        else:
            ng = m
    return ok

def binsearch_right(a, x):
    ng = -1
    ok = len(a)
    while abs(ok-ng)>1:
        m = (ng+ok)//2
        if x<a[m]:
            ok = m
        else:
            ng = m
    return ok

def dijkstra(G, s):
    que = []
    d = [INF]*len(G)
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
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

def kruskal(es, V):
    es.sort(key=lambda x:x[2])
    uf = UnionFind(V)
    res = 0
    for e in es:
        if not uf.same(e[0], e[1]):
            uf.unite(e[0], e[1])
            res += e[2]
    return res

def lis(a):
    dp = [INF]*len(a)
    for i in a:
        dp[bisect.bisect_left(dp, i)] = i
    return bisect.bisect_left(dp, INF)
