import bisect, collections, copy, heapq, itertools, math, string, sys, datetime
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
    YMD = SS()
    Y = int(YMD[:4])
    M = int(YMD[5:7])
    D = int(YMD[8:])

    d = datetime.date(Y, M, D)
    td = datetime.timedelta(days=1)

    while True:
        year = d.year
        month = d.month
        day = d.day
        if year % month == 0:
            if year // month % day == 0:
                print(d.strftime('%Y/%m/%d'))
                break
        d += td

if __name__ == '__main__':
    resolve()
