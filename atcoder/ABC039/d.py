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
    H, W = LI()
    S = [list(SS()) for _ in range(H)]

    # 隣接画素が全て#な画素は#として収縮前画像を生成
    ans = [['.'] * W for _ in range(H)]

    for y, x in itertools.product(range(H), range(W)):
        cnt = 0
        for dy, dx in itertools.product((-1, 0, 1), repeat=2):
            ny = y + dy
            nx = x + dx
            if 0 <= ny < H and 0 <= nx < W:
                if S[ny][nx] != '#':
                    cnt += 1
        if cnt == 0:
            ans[y][x] = '#'

    # 収縮前画像を再度収縮して入力と比較
    S_ = [['.'] * W for _ in range(H)]
    for y, x in itertools.product(range(H), range(W)):
        cnt = 0
        for dy, dx in itertools.product((-1, 0, 1), repeat=2):
            ny = y + dy
            nx = x + dx
            if 0 <= ny < H and 0 <= nx < W:
                if ans[ny][nx] == '#':
                    cnt += 1
        if cnt > 0:
            S_[y][x] = '#'

    if S_ == S:
        print('possible')
        for i in ans:
            print(''.join(i))
    else:
        print('impossible')


if __name__ == '__main__':
    resolve()
