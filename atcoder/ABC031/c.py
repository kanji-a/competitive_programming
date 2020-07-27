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
    a = LI()

    # Nが小さいので、毎回得点計算の足し算してOK
    score_t_max = -INF
    for i in range(N):
        # 高橋君の○を決めて青木君の得点が最大になる場合の高橋君の得点
        score_t_max_tmp = -INF
        score_a_max = -INF
        for j in range(N):
            if i != j:
                l = min(i, j)
                h = max(i, j)
                score_t = 0
                score_a = 0
                for k in range(h + 1 - l):
                    if k % 2 == 0:
                        score_t += a[l+k]
                    else:
                        score_a += a[l+k]
                if score_a > score_a_max:
                    score_a_max = score_a
                    score_t_max_tmp = score_t
        score_t_max = max(score_t_max_tmp, score_t_max)

    print(score_t_max)

if __name__ == '__main__':
    resolve()
