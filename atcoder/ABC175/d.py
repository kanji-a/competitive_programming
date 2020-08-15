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
    N, K = LI()
    P = LI_()
    C = LI()

    ans = -INF
    for i in range(N):
        visited = [False] * N
        c = i
        loop = [c]
        while True:
            visited[c] = True
            c = P[c]
            if visited[c]:
                break
            loop.append(c)
        # print(loop)
        len_loop = len(loop)
        l  = [C[i] for i in loop]
        score_loop = sum(l)

        tmp = 0
        # ループさせる場合のその分の加算
        if K > len_loop and score_loop > 0:
            tmp += K // len_loop * score_loop

        # ループではない部分
        K_no_loop =  K if K == len_loop else K % len_loop
        # print(l)
        l_cum = [0] * (len_loop + 1)
        for j in range(len_loop):
            l_cum[j+1] = l[j] + l_cum[j]
        # print(l_cum)

        max_cand = -INF
        for j in range(K_no_loop):
            for k in range(len_loop - j):
                # print(j+k+1, k)
                max_cand = max(l_cum[j+k+1] - l_cum[k], max_cand)
        tmp += max_cand

        ans = max(tmp, ans)

    print(ans)

if __name__ == '__main__':
    resolve()
