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
    K = I()

    if K % 2 == 0 or K % 5 == 0:
        print(-1)
    else:
        rem = 7 % K
        ans = 0
        while rem != 0:
            rem = rem * 10 + 7
            rem %= K
            ans += 1

        print(ans + 1)

if __name__ == '__main__':
    resolve()
