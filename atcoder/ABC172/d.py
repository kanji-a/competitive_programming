import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
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

    primes = sieve(N)
    d = [2] * (N + 1)
    d[1] = 1

    for i in range(2, int(N**0.5)+1):
        for j in range(i * 2, N + 1, i):
            if i ** 2 == j:
                d[j] += 1
            else:
                d[j] += 2

    d0 = [1] * (N + 1)
    # d0[1] = 1
    for i in range(2, N+1):
        for j in range(i, N + 1, i):
            d0[j] += 1


    ans = 0
    for i in range(1, N + 1):
        ans += i * d0[i]

    print(d)
    print(d0)
    print(ans)

if __name__ == '__main__':
    resolve()
