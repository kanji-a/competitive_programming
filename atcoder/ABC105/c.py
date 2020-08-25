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

    if N == 0:
        print(0)
    else:
        ans = []
        while abs(N) > 0:
            r = N % 2
            ans.append(r)
            if r == 1:
                N -= 1
            N //= -2

        print(''.join([str(i) for i in reversed(ans)]))

if __name__ == '__main__':
    resolve()
