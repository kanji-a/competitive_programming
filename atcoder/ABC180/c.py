import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 10**9+7
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N = I()

    ans_half = [i for i in range(1, int(N ** 0.5) + 1) if N % i == 0]
    for i in ans_half:
        print(i)
    for i in reversed(ans_half):
        if i ** 2 != N:
            print(N // i)

if __name__ == '__main__':
    resolve()
