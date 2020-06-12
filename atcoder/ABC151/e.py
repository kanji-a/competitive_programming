N, K = map(int, input().split())
A = list(map(int, input().split()))
A = sorted(A)
mod = 10**9+7

# conbModに使うfactとfactinvを求める
def factorialMod(n, p):
    fact = [1, 1]
    factinv = [1, 1]
    inv = [0, 1]
    for i in range(2, n + 1):
        fact.append((fact[-1] * i) % p)
        inv.append((-inv[p % i] * (p // i)) % p)
        factinv.append((factinv[-1] * inv[-1]) % p)
    return fact, factinv

# 二項係数を素数で割った余り
def combMod(n, r, fact, factinv, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

ans = 0
fact, factinv = factorialMod(N, mod)
for i in range(N):
    num = combMod(i, K-1, fact, factinv, mod) % mod
    ans += num * A[i] % mod
    ans -= num * A[N-i-1] % mod
    ans %= mod

print(ans)