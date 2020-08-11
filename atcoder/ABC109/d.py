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
    a = [LI() for _ in range(H)]

    ans = []
    # 奇数枚の山のコインを右の山に移動
    if W >= 2:
        for i in range(H):
            for j in range(W - 1):
                if a[i][j] % 2 == 1:
                    a[i][j] -= 1
                    a[i][j+1] += 1
                    ans.append((i + 1, j + 1, i + 1, j + 2))

    # 一番右の列の奇数枚の山のコインを下の山に移動
    if H >= 2:
        for i in range(H - 1):
            if a[i][-1] % 2 == 1:
                a[i][-1] -= 1
                a[i+1][-1] += 1
                ans.append((i + 1, W, i + 2, W))

    # for i in a:
    #     print(*i)

    print(len(ans))
    if ans:
        for i in ans:
            print(*i)

if __name__ == '__main__':
    resolve()
