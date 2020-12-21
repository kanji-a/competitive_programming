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
    T = I()
    for _ in range(T):
        N, S, K = LI()
        # 一周する前に座れず、元の席に戻ってきたら座れない
        if (N - S) % K == 0:
            # 一周せずに行けた場合
            print((N - S) // K)
        else:
            ans = (N * k - S) // K
            print(ans)
            
if __name__ == '__main__':
    resolve()
