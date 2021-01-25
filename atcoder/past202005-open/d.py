import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
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
    N = I()
    s = [SS() for _ in range(5)]

    # 特徴的な点灯箇所で場合分け
    ans = []
    for i in range(N):
        init = 4 * i + 1
        if s[0][init] == '.':
            ans.append('1')
        elif s[0][init+1] == '.':
            ans.append('4')
        elif s[4][init] == '.':
            ans.append('7')
        elif s[2][init+1] == '.':
            ans.append('0')
        else:
            # 235689は似てるので4箇所で判定
            d = {}
            d[('.', '#', '#', '.')] = '2'
            d[('.', '#', '.', '#')] = '3'
            d[('#', '.', '.', '#')] = '5'
            d[('#', '.', '#', '#')] = '6'
            d[('#', '#', '#', '#')] = '8'
            d[('#', '#', '.', '#')] = '9'
            key = (s[1][init], s[1][init+2], s[3][init], s[3][init+2])
            ans.append(d[key])

    print(''.join(ans))

if __name__ == '__main__':
    resolve()
