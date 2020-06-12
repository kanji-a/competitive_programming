import sys, collections
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**20
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def resolve():
    N = I()

    def sieve(n):
        is_prime = [True for _ in range(n+1)]
        is_prime[0] = False
        is_prime[1] = False
        for i in range(2, int(n**0.5)+1):
            if is_prime[i]:
                for j in range(i*2, n+1, i):
                    is_prime[j] = False
        return [i for i in range(n+1) if is_prime[i]]

    primes = sieve(int(N**0.5))

    ans = []
    temp = N
    for i in primes:
        j = i
        while j<int(N**0.5)+1:
            if temp%j == 0:
                ans.append(j)
                temp //= j
            j *= i
    if temp > int(N**0.5):
        ans.append(temp)

    # print(ans)
    print(len(ans))

if __name__ == '__main__':
    resolve()