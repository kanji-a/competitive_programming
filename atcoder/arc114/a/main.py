#!/usr/bin/env python3
import bisect, collections, copy, functools, heapq, itertools, math, operator, string, sys, typing
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)
INF = float('inf')
MOD = 10 ** 9 + 7
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def sieve(n):
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*2, n+1, i):
                is_prime[j] = False
    return [i for i in range(n+1) if is_prime[i]]

def resolve():
    N = I()
    X = LI()

    # Xの素因数を全部列挙 それらの1個ずつの積で一番小さいのが答え
    primes = sieve(50)
    len_primes = len(primes)
    ans = INF
    for i in range(2 ** len_primes):
        tmp = 1
        for j in range(len_primes):
            if i >> j & 1:
                tmp *= primes[j]
        is_ok = True
        for j in X:
            if math.gcd(tmp, j) == 1:
                is_ok = False
        if is_ok:
            ans = min(tmp, ans)

    print(ans)

if __name__ == '__main__':
    resolve()
