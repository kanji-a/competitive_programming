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
    X = SS()

    stk = []

    len_X = len(X)
    ans = len_X
    for i in range(len_X):
        if X[i] == 'S':
            stk.append('S')
        else:
            if stk and stk[-1] == 'S':
                stk.pop()
                ans -= 2

    print(ans)

if __name__ == '__main__':
    resolve()
