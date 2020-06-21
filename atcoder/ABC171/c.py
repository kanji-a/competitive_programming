import sys, collections, bisect, itertools, heapq, math, copy, string
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
    N = I() - 1

    ans = ''
    while N >= 26:
        ans += string.ascii_lowercase[N%26]
        N = N // 26 - 1
    ans += string.ascii_lowercase[N%26]

    print(ans[::-1])

if __name__ == '__main__':
    resolve()
