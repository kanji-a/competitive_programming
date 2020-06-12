import sys
input = lambda: sys.stdin.readline().rstrip() 

def combMod(n, r, p):
    numer = 1
    denom = 1
    for i in range(1, r+1):
        numer = numer * (n-r+i) % p
        denom = denom * i % p
    return numer * pow(denom, p-2, p) % p

def resolve():
    n, a, b = map(int, input().split())
    mod = 10**9+7
    print((pow(2, n, mod) - 1 - combMod(n, a, mod) - combMod(n, b, mod)) % mod)

if __name__ == '__main__':
    resolve()
