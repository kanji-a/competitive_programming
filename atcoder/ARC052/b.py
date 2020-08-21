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
    N, Q = LI()
    XRH = [LI() for _ in range(N)]
    max_B = 2 * 10 ** 4

    # [i, m)の右側累積和
    cum = [0] * (max_B + 1)
    for xrh in XRH:
        x, r, h = xrh
        v = (math.pi * r ** 2) * h / 3
        for i in range(max_B):
            if 0 <= i < x:
                cum[i] += v
            elif x <= i < x + h:
                cum[i] += v * ((x + h - i) / h) ** 3
    # print(cum)

    for _ in range(Q):
        A, B = LI()
        print(cum[A] - cum[B])


if __name__ == '__main__':
    resolve()
