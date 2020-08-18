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
    A, B = LI()
    P = LI()

    ans = [0] * 3
    for i in P:
        if i <= A:
            ans[0] += 1
        elif A + 1 <= i <= B:
            ans[1] += 1
        else:
            ans[2] += 1

    print(min(ans))

if __name__ == '__main__':
    resolve()
