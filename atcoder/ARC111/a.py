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
    N, M = LI()

    # ans = 10 ** N // M % M
    # print(ans)
    # 分子と分母が互いに素か
    if M % 2 == 0 or M % 5 == 0:
        # 互いに素でない場合
        print('aaa')
    else:
        ans = pow(10, N, M) % M
        print(ans)


if __name__ == '__main__':
    resolve()
