import sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**20
MOD = 10**5
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def resolve():
    n, m = LI()
    s = [I() for _ in range(n-1)]
    a = [I() for _ in range(m)]

    acc = [0]*n
    for i in range(n-1):
        acc[i+1] = acc[i]+s[i]
    # print(acc)

    ans = 0
    city = 0
    for i in a:
        ans += abs(acc[city+i]-acc[city])
        city += i
    print(ans%MOD)

if __name__ == '__main__':
    resolve()