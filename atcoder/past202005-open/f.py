import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
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
    a = [set(SS()) for _ in range(N)]

    ans_half = []
    for i in range(N // 2):
        common = a[i] & a[N-1-i]
        if not common:
            print(-1)
            return 
        ans_half.append(common.pop())
    ans_half = ''.join(ans_half)

    if N % 2 == 0:
        print(ans_half + ans_half[::-1])
    else:
        print(ans_half + a[N//2].pop() + ans_half[::-1])

if __name__ == '__main__':
    resolve()
