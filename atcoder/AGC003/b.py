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
    N = I()
    A = [I() for _ in range(N)]

    # 奇数個の山同士を相殺して偶数個の山にした後同数字ペアを作る
    # 奇数個の山の間に0個の山が無ければ全て取れる
    # 言い換えれば0個の山の間は0,1個残しで取り切れる
    A_cum = [0] * (N + 1)
    zero = [0]
    for i in range(N):
        A_cum[i+1] = A_cum[i] + A[i]
        if A[i] == 0:
            zero.append(i)
    zero.append(N)

    ans = 0
    for i in range(len(zero) - 1):
        ans += (A_cum[zero[i+1]] - A_cum[zero[i]]) // 2

    print(ans)

if __name__ == '__main__':
    resolve()
