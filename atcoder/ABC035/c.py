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
    b = [0] * (N + 1)
    for _ in range(Q):
        l, r = LI()
        b[l-1] += 1
        b[r] -= 1

    b_cum = [0] * (N + 2)
    for i in range(N):
        b_cum[i+1] = b_cum[i] + b[i]

    ans = []
    for i in range(N):
        ans.append(str(b_cum[i+1] % 2))

    print(''.join(ans))

if __name__ == '__main__':
    resolve()
