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
    A = LI()

    A.sort()
    divisible = set(list(range(1, 10**6+1)))

    for i in A:
        j = 1
        while i*j <= 10**6:
            if i*j in divisible:
                divisible.remove(i*j)
                j += 1

    ans = 0
    for i in A:
        if j in divisible:
            ans += 1
        
    print(ans)

if __name__ == '__main__':
    resolve()