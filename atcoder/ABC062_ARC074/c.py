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

    ans = INF
    if H % 3 == 0 or W % 3 == 0:
        ans = 0
    else:
        # 同方向に分割する場合
        ans = min(H, W)

        # 分割方向を変える場合
        s = [0] * 3
        # 縦→横の場合と横→縦の場合
        for _ in range(2):
            s[0] = H * (W // 3)
            s[1] = (W - W // 3) * (H // 2)
            s[2] = (W - W // 3) * (H - H // 2)
            ans = min(max(s)- min(s), ans)
            s[0] = H * (W // 3 + 1)
            s[1] = (W - (W // 3 + 1)) * (H // 2)
            s[2] = (W - (W // 3 + 1)) * (H - H // 2)
            ans = min(max(s)- min(s), ans)
            H, W = W, H
       
    print(ans)

if __name__ == '__main__':
    resolve()
