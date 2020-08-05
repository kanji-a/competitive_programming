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
    S = [int(i) for i in SS()]
    N = len(S)

    ans0 = 0
    ans1 = 0
    for i in range(N):
        ans0 += abs(S[i] - i % 2)
        ans1 += abs(S[i] - (1 - i % 2))

    print(min(ans0, ans1))

if __name__ == '__main__':
    resolve()
