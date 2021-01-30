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

    # a〜a+l-1までの和
    # (2*a+l-1)*l=2*Nを満たす(a,l)の数
    ans = 0

    divisor = set()
    for i in range(1, int((2 * N) ** 0.5) + 1):
        if (2 * N) % i == 0:
            divisor.add(i)
            divisor.add((2 * N) // i)

    for i in divisor:
        if (2 * N) % i == 0:
            tmp = (2 * N) // i
            if (tmp - i + 1) % 2 == 0:
                ans += 1

    print(ans)

if __name__ == '__main__':
    resolve()
