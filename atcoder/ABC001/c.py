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
    Deg, Dis = LI()

    d = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
    Dir = d[(Deg * 2 + 225) % 7200 // (7200 // 16)]

    # 四捨五入してボーダーになる値の最小値*60 (ex. 0.3→0.25*60=15)
    l = [0, 15, 93, 201, 327, 477, 645, 831, 1029, 1245, 1467, 1707, 1959]
    W = bisect.bisect_right(l, Dis) - 1
    if W == 0:
        Dir = 'C'

    print(Dir, W)

if __name__ == '__main__':
    resolve()
