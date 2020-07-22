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

    # 文字同士のindexの隙間の最大値の最小値

    len_s = len(s)

    # 文字毎のindex
    idx = [[] for _ in range(26)]
    for i in range(len_s):
        idx[ord(s[i]) - ord('a')].append(i)

    # 文字毎のindexの間の文字数
    idx_gap = [[] for _ in range(26)]
    for i in range(26):
        if len(idx[i]) >= 1:
            idx_gap[i].append(idx[i][0])
            idx_gap[i].append(len_s - idx[i][-1] - 1)
            if len(idx[i]) >= 2:
                for j in range(len(idx[i]) - 1):
                    idx_gap[i].append(idx[i][j+1] - idx[i][j] - 1)

    print(min([max(i) for i in idx_gap if i]))

if __name__ == '__main__':
    resolve()
