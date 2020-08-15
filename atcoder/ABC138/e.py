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
    s = SS()
    t = SS()

    len_s = len(s)
    len_t = len(t)

    # アルファベットのs内のindex一覧
    l = [[] for _ in range(26)] 
    for i in range(len_s):
        l[ord(s[i]) - ord('a')].append(i)
    # print(l)

    if len([i for i in t if i in set(s)]) == len_t:
        # t内の文字がs内の何番目に登場するか
        t_idx = [l[ord(i)-ord('a')] for i in t]
        # print(t_idx)

        # 昇順部分がなるべく多くなるようにindexを選ぶ
        t_idx_best = [t_idx[0][0]]
        for i in range(1, len_t):
            p = t_idx_best[-1]
            idx = bisect.bisect_left(t_idx[i], p)
            if idx == len(t_idx[i]):
                t_idx_best.append(t_idx[i][0])
            else:
                t_idx_best.append(t_idx[i][idx])
        # print(t_idx_best)

        # 昇順じゃないところでsがもう一個必要になる
        ans = 0
        for i in range(len_t - 1):
            if t_idx_best[i] >= t_idx_best[i+1]:
                ans += len_s
        ans += t_idx_best[-1] + 1
        print(ans)

    else:
        print(-1)

if __name__ == '__main__':
    resolve()
