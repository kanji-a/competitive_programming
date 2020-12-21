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
    A = LI()
    # ソートしても答えは同じ
    A.sort()

    A_acm = list(itertools.accumulate(A, initial=0))

    # ソートしたことで絶対値を外せる
    # 絶対値を外して内側のΣを展開、これで1重ループに
    ans = 0
    for i in range(N):
        ans += (A_acm[-1] - A_acm[i+1]) - (N - 1 - i) * A[i]
        
    print(ans)

if __name__ == '__main__':
    resolve()
