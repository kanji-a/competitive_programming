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
    s = SS()

    # AがBCを乗り越えて右に進むイメージ
    # それぞれのAに対して右側に連続したBCがいくつあるか
    ans = 0
    len_s = len(s)
    cnt = 0
    i = 0
    while i < len_s:
        if s[i] == 'A':
            cnt += 1
            i += 1
        elif i + 1 < len_s and s[i] == 'B' and s[i+1] == 'C':
            ans += cnt
            i += 2
        else:
            cnt = 0
            i += 1
            
    print(ans)

if __name__ == '__main__':
    resolve()
