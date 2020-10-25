import bisect, collections, copy, decimal, heapq, itertools, math, string, sys
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
    X, Y = LI()

    if Y == 0:
        print('ERROR')
    else:
        ans = decimal.Decimal(X / Y).quantize(decimal.Decimal('1.00'), rounding=decimal.ROUND_DOWN)
        print(ans)

if __name__ == '__main__':
    resolve()
