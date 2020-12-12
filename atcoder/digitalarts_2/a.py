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
    s = LSS()
    N = I()
    t = [SS() for _ in range(N)]

    ans = [list(i) for i in s]

    for i in range(len(s)):
        for j in t:
            len_s_i = len(s[i])
            if len_s_i == len(j):
                is_match = True
                for k in range(len_s_i):
                    if j[k] != '*' and j[k] != s[i][k]:
                        is_match = False
                        break
                if is_match:
                    ans[i] = ['*'] * len_s_i

    print(*[''.join(i) for i in ans])


if __name__ == '__main__':
    resolve()
