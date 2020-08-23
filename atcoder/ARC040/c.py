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
    S = [list(SS()) for _ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(N - 1, -1, -1):
            # 最右.を見つけたらその下の行を右に塗っていく
            # その行はもう見ないので塗る処理はしない
            if S[i][j] == '.':
                if i < N - 1:
                    for k in range(j, N):
                        S[i+1][k] = 'o'
                cnt += 1
                break

    # for i in S:
    #     print(i)
    print(cnt)

if __name__ == '__main__':
    resolve()
