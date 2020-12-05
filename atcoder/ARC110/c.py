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
    P = LI()

    # 1から順番に左に詰めていくしかない
    # 実際にやってみて、同じ操作が出たらアウト、最後に使ってない交換をチェック
    ans = []
    used = [False] * (N - 1)
    idx = [-1] * (N + 1)
    for i in range(N):
        idx[P[i]] = i

    cur = 1
    while True:
        if cur == N:
            break
        i = idx[cur] 
        if i != cur - 1:
            # 揃ってなかった場合
            if used[i-1]:
                break
            used[i-1] = True
            ans.append(i-1)
            idx[cur], idx[P[i-1]] = idx[P[i-1]], idx[cur]
            P[i-1], P[i] = P[i], P[i-1]
        else:
            # 揃ってた場合
            cur += 1

    if used.count(False) == 0 and P == sorted(P):
        for i in ans:
            print(i + 1)
    else:
        print(-1)

if __name__ == '__main__':
    resolve()
