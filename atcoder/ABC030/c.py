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
    N, M = LI()
    X, Y = LI()
    a = LI()
    b = LI()

    ans = 0
    t = 0
    idx_a = 0
    idx_b = 0
    while True:
        if t > a[-1]:
            break
        while idx_a + 1 < N and a[idx_a] < t:
            idx_a += 1
        t = a[idx_a] + X

        if t > b[-1]:
            break
        while idx_b + 1 < M and b[idx_b] < t:
            idx_b += 1
        t = b[idx_b] + Y

        ans += 1
    
    print(ans)

if __name__ == '__main__':
    resolve()
