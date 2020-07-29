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
    m_d = []
    for i in range(N):
        md = SS()
        i_s = md.index('/')
        m_d.append((int(md[:i_s]), int(md[i_s+1:])))

    days_num = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    days_num_cum = [0] * 13
    for i in range(12):
        days_num_cum[i+1] = days_num_cum[i] + days_num[i]

    holidays = [i % 7 in (0, 6) for i in range(366)]
    for m, d in m_d:
        day = days_num_cum[m-1] + (d - 1)
        while day + 1 <= 366:
            if not holidays[day]:
                holidays[day] = True
                break
            day += 1

    ans = 0
    cnt = 0
    for i in holidays:
        if i:
            cnt += 1
        else:
            ans = max(cnt, ans)
            cnt = 0
    ans = max(cnt, ans)

    print(ans)

if __name__ == '__main__':
    resolve()
