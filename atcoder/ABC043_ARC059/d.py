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
    len_s = len(s)

    acm = {k: [0] * (len_s + 1) for k in string.ascii_lowercase}
    for i in range(len_s):
        for j in string.ascii_lowercase:
            if j == s[i]:
                acm[j][i+1] = acm[j][i] + 1
            else:
                acm[j][i+1] = acm[j][i]
    for i in acm.items():
        print(i)

    # 各文字ごとに、過半数を超える区間があるか見ていく
    for i in string.ascii_lowercase:
        for j in range(len_s):
            num_b = acm[i][j]
            idx = bisect.bisect_left(acm[i], num_b - )


if __name__ == '__main__':
    resolve()
