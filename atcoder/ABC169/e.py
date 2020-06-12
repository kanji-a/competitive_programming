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
    A = []
    B = []
    for _ in range(N):
        a, b = LI()
        A.append(a)
        B.append(b)

    A.sort()
    B.sort()

    A_med = 0
    B_med = 0
    if N%2==0:
        A_med_2 = (A[N//2-1] + A[N//2])
        B_med_2 = (B[N//2-1] + B[N//2])
        print((B_med_2-A_med_2)+1)
    else:
        A_med_2 = A[(N+1)//2-1]*2
        B_med_2 = B[(N+1)//2-1]*2
        print((B_med_2-A_med_2)//2+1)

if __name__ == '__main__':
    resolve()
