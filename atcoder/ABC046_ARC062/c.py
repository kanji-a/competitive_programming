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

def resolve():
    N = I()
    TA = [LI() for _ in range(N)]

    t, a = TA[0]
    for i in range(1, N):
        T, A = TA[i]
        # t/T>a/A
        if t * A > a * T:
            rate = (t - 1) // T + 1
            t = T * rate
            a = A * rate
        else:
            rate = (a - 1) // A + 1
            t = T * rate
            a = A * rate

    print(t + a)

if __name__ == '__main__':
    resolve()
