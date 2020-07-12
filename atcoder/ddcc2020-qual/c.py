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
    H, W, K = LI()
    s = [SS() for _ in range(H)]

    ans = [[0] * W for _ in range(H)]

    # 行ごとにいちごで区切って塗り分け
    cnt = 1
    for i in range(H):
        is_first = True
        if s[i].count("#") >= 1:
            for j in range(W):
                if s[i][j] == '#':
                    if is_first:
                        is_first = False
                    else:
                        cnt += 1
                ans[i][j] = cnt
            cnt += 1

    # いちごなし行の場合、前の行の値をコピー
    first_strawberry_row = -1
    for i in range(H):
        if s[i].count("#") >= 1:
            first_strawberry_row = i
            break

    for i in range(first_strawberry_row, H):
        if s[i].count("#") == 0:
            for j in range(W):
                ans[i][j] = ans[i-1][j]

    # 前にコピー元がない場合、後ろの行からコピー
    for i in range(first_strawberry_row):
        r = first_strawberry_row - 1 - i
        if s[r].count("#") == 0:
            for j in range(W):
                ans[r][j] = ans[r+1][j]

    for i in ans:
        print(*i)

if __name__ == '__main__':
    resolve()
