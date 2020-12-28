import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 10 ** 9 + 7
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N = I()
    C = [I() for _ in range(N)]

    idx = collections.defaultdict(list)
    for i in range(N):
        idx[C[i]].append(i)
    # print(idx)

    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(N):
        # まず、手前までの分
        dp[i+1] = dp[i]
        # 手前が同じ数字だったら場合の数は増えない
        # 今見ている数字を見たことで、左にある同じ数字までをひっくり返すという場合が増える
        if C[i] != C[i-1]:
            for j in idx[C[i]]:
                if j >= i - 1:
                    break
                dp[i+1] += dp[j]
    # print(dp)

    ans = dp[-1]
    print(ans)

if __name__ == '__main__':
    resolve()
