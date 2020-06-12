import sys, bisect
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

    AA = list(sorted([i+1+A[i] for i in range(N)]))

    ans = 0
    for i in range(N):
        idx_l = bisect.bisect_left(AA, i+1-A[i])
        idx_r = bisect.bisect_right(AA, i+1-A[i])
        num = 0
        if 0<=idx_l<N and 0<=idx_r<N:
            num = idx_r - idx_l
        ans += num

    print(ans)

if __name__ == '__main__':
    resolve()
