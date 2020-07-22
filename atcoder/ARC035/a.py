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

    len_s = len(s)
    ans = 'YES'
    for i in range(len(s)):
        if (s[i] != '*' and s[len_s-1-i] != '*') and s[i] != s[len_s-1-i]:
            ans = 'NO'

    print(ans)

if __name__ == '__main__':
    resolve()
