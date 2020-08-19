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
    m = I()

    VV = ''
    if m < 100:
        VV = '00'
    elif 100 <= m <= 5000:
        VV = '{:02d}'.format(m // 100)
    elif 6000 <= m <= 30000:
        VV = (m + 50000) // 1000
    elif 35000 <= m <= 70000:
        VV = (m + 370000) // 5000
    elif 70000 < m:
        VV = 89

    print(VV)

if __name__ == '__main__':
    resolve()
