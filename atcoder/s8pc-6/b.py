import sys, itertools
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
    AB = [LI_() for _ in range(N)]

    ans = INF
    for i, j in itertools.product([i[0] for i in AB], [i[1] for i in AB]):
        time_sum = 0
        for k in AB:
            time_sum += abs(i-k[0])+abs(k[1]-k[0])+abs(k[1]-j)
        ans = min(time_sum, ans)
    print(ans)

if __name__ == '__main__':
    resolve()