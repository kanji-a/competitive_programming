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
    a = [SS() for _ in range(H)]

    white_columun = set()
    for c in range(W):
        cnt = 0
        for r in range(H):
            if a[r][c] == '.':
                cnt += 1
        if cnt == H:
            white_columun.add(c)

    for i in a:
        if i.count('.') < W:
            ans = []
            for j in range(W):
                if not j in white_columun:
                    ans.append(i[j])
            print(''.join(ans))

if __name__ == '__main__':
    resolve()
