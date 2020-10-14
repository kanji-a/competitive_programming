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
    s = SS()
    t = SS()
    len_s = len(s)
    len_t = len(t)

    dp = [[0] * (len_t + 1) for _ in range(len_s + 1)]
    for i in range(1, len_s + 1):
        for j in range(1, len_t + 1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    # for i in dp:
    #     print(i)
    
    i, j = len_s, len_t
    ans_r = []
    while i > 0 and j > 0:
        if s[i-1] == t[j-1]:
            ans_r.append(s[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] == dp[i][j]:
            i -= 1
        else:
            j -= 1

    print(''.join(ans_r[::-1]))

if __name__ == '__main__':
    resolve()
