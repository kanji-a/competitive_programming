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
    N, K = LI()
    t = [I() for _ in range(N)]

    s = t[0] + t[1]

    ans = -1
    for i in range(N - 2):
        s += t[i+2]
        if s < K:
            ans = i + 3
            break
        s -= t[i] 

    print(ans)

if __name__ == '__main__':
    resolve()
