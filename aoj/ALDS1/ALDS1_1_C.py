import sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**10
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    n = I()
    A = [I() for _ in range(n)]

    def is_prime(n):
        if n==0 or n==1: return False
        for i in range(2, int(n**0.5)+1):
            if n%i==0:
                return False
        return True

    print([is_prime(i) for i in A].count(True))

if __name__ == '__main__':
    resolve()