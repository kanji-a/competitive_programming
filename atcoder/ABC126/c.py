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

    ans = 0
    for i in range(1, N + 1):
        tmp = 1 / N
        score = i
        while 1 <= score <= K - 1:
            score *= 2
            tmp *= 0.5
        ans += tmp

    print(ans)

if __name__ == '__main__':
    resolve()
