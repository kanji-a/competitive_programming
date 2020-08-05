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

def resolve():
    N, P = LI()

    pf = primeFactorization(P)
    ans = 1
    for k, v in pf.items():
        ans *= k ** (v // N)

    print(ans)

if __name__ == '__main__':
    resolve()
