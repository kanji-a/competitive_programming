import collections

N = int(input())
A = list(map(int, input().split()))

mod = 10**9+7

def sieve(n):
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*2, n+1, i):
                is_prime[j] = False
    return [i for i in range(n+1) if is_prime[i]]

primes = sieve(10**3)

def primeFactorization(n):
    ans = []
    temp = n
    for p in primes:
        while temp%p == 0:
            ans.append(p)
            temp //= p
    if temp > 1:
        ans.append(temp)
    return collections.Counter(ans)

AFactorized = list(map(primeFactorization, A))

lcm = collections.Counter()
for a in AFactorized:
    for p, n in a.items():
        lcm[p] = max(lcm[p], n)

lcm_val = 1
for p, n in lcm.items():
    lcm_val *= pow(p, n, mod)

ans = 0
for a in A:
    ans += lcm_val * pow(a, mod-2, mod)
    ans %= mod

print(ans)