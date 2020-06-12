import sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**20
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def resolve():
    H, W, K, V = LI()
    A = [LI() for _ in range(H)]

    acc = [[0]*W for _ in range(H+1)]
    for i in range(H):
        for j in range(W):
            acc[i+1][j] = acc[i][j] + A[i][j] + K

    # 縦幅を決める、オフセットを決める、横にしゃくとり法
    max_area = 0
    for height in range(1, H+1):
        max_max_width = 0
        for offset in range(H-height+1):
            r = 0
            max_width = 0
            cost = 0
            for l in range(W):
                while r<W and cost+(acc[offset+height][r]-acc[offset][r])<=V:
                    cost += acc[offset+height][r] - acc[offset][r]
                    r += 1
                max_width = max(r-l, max_width)
                if r==l:
                    r += 1
                else:
                    cost -= acc[offset+height][l] - acc[offset][l]
            max_max_width = max(max_width, max_max_width)
        max_area = max(height*max_max_width, max_area)

    print(max_area)

if __name__ == '__main__':
    resolve()