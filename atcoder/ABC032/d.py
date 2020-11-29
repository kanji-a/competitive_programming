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
    N, W = LI()
    vw = [LI() for _ in range(N)]
    max_v = max([i[0] for i in vw])
    sum_v = sum([i[0] for i in vw])
    max_w = max([i[1] for i in vw])
    sum_w = sum([i[1] for i in vw])

    if N <= 30:
        n_half = N // 2
        a_f = collections.defaultdict(int)
        a_b = collections.defaultdict(int)
        for i in range(2 ** n_half):
            tmp_v = 0
            tmp_w = 0
            for j in range(n_half):
                if i >> j & 1:
                    tmp_v += vw[j][0]
                    tmp_w += vw[j][1]
            if tmp_w <= W:
                a_f[tmp_w] = max(tmp_v, a_f[tmp_w])
        for i in range(2 ** (N - n_half)):
            tmp_v = 0
            tmp_w = 0
            for j in range(N - n_half):
                if i >> j & 1:
                    tmp_v += vw[n_half+j][0]
                    tmp_w += vw[n_half+j][1]
            if tmp_w <= W:
                a_b[tmp_w] = max(tmp_v, a_b[tmp_w])
        a_b_w = sorted(list(a_b.keys()))
        # 二分探索で重さギリギリのものを選択するので、それより軽いものよりも価値が小さいような組み合わせは除外する
        m = 0
        for i in a_b_w:
            if a_b[i] < m:
                a_b.pop(i)
            else:
                m = a_b[i]
        a_b_w = sorted(list(a_b.keys()))

        ans = 0
        for k, v in a_f.items():
            idx = bisect.bisect_right(a_b_w, W - k)
            if idx - 1 >= 0:
                ans = max(a_b[a_b_w[idx-1]] + v , ans)
        print(ans)

    elif max_v <= 1000:
        dp = [INF] * (sum_v + 1)
        dp[0] = 0
        for i in range(N):
            for j in range(sum_v, -1, -1):
                v, w = vw[i]
                if j - v >= 0:
                    dp[j] = min(dp[j-v] + w, dp[j])
        ans = max([i for i, e in enumerate(dp) if e <= W])
        print(ans)

    else:
        dp = [0] * (sum_w + 1)
        for i in range(N):
            for j in range(sum_w, -1, -1):
                v, w = vw[i]
                if j - w >= 0:
                    dp[j] = max(dp[j-w] + v, dp[j])
        ans = max(dp[:W+1])
        print(ans)

if __name__ == '__main__':
    resolve()
