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
    a = LI()

    b = [0] * N
    for i in range(N):
        # (N-1-i)*2以降を全部足したのをaから引く
        tmp = 0
        for j in range(N - 1 - i, N, N - i):
            tmp ^= b[j]
        b[N-1-i] = tmp ^ a[N-1-i]

    m = b.count(1)
    print(m)
    if m >= 1:
        ans = []
        for i, e in enumerate(b):
            if e == 1:
                ans.append(i + 1)
        print(*ans)

if __name__ == '__main__':
    resolve()
