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

    primes = sieve(55555)
    # 1の位が同じ数字を5つ集めれば5の倍数になる
    ans = [i for i in primes if i % 10 == 3]
    print(*ans[:N])

if __name__ == '__main__':
    resolve()
