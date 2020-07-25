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
    x, y, W = LSS()
    c = [list(SS()) for _ in range(9)]

    d = {}
    d['R'] = (0, 1)
    d['L'] = (0, -1)
    d['U'] = (-1, 0)
    d['D'] = (1, 0)
    d['RU'] = (-1, 1)
    d['RD'] = (1, 1)
    d['LU'] = (-1, -1)
    d['LD'] = (1, -1)

    c_ex = [i[3:0:-1] + i + i[-2:-5:-1] for i in c]
    c_ex = c_ex[3:0:-1] + c_ex + c_ex[-2:-5:-1]

    x = int(x) + 2
    y = int(y) + 2

    ans = []
    for _ in range(4):
        ans.append(c_ex[y][x])
        y += d[W][0]
        x += d[W][1]

    print(''.join(ans))

if __name__ == '__main__':
    resolve()
