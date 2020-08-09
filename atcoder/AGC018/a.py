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
    N, K = LI()
    A = LI()

    # 互いに素なペアがあれば、1を作れる
    # 1があればmax(A)以下の数字を作れる
    gcd = A[0]
    for i in A:
        gcd = math.gcd(gcd, i)

    if K % gcd == 0 and K <= max(A):
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')

if __name__ == '__main__':
    resolve()
