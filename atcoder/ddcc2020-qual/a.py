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
    X, Y = LI_()

    reward = (300000, 200000, 100000, 0)

    ans = reward[min(X, 3)] + reward[min(Y, 3)] + (400000 if X == Y == 0 else 0)
    print(ans)

if __name__ == '__main__':
    resolve()
