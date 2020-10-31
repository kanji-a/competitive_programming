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
    N, K = LI()
    a = LI()

    # dp[i]: i個の山をもらって勝てるかどうか
    dp = [False] * (K + 1)
    dp[0] = False

    for i in range(1, K + 1):
        for j in a:
            # 現状態から遷移可能な状態に、もらったら負ける状態が合った場合、
            # それを相手に押し付けられるということなので勝ち
            if i - j >= 0 and not dp[i-j]:
                dp[i] = True
                break
    # print(dp)

    if dp[-1]:
        print('First')
    else:
        print('Second')

if __name__ == '__main__':
    resolve()
