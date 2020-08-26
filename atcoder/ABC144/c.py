import sys
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

    fact = []
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            fact.append((i, N // i))

    print(sum(fact[-1]) - 2)

if __name__ == '__main__':
    resolve()
