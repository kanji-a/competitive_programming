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
    R, G, B, N = LI()

    ans = 0
    for r in range(N // R + 1):
        for g in range((N - R * r) // G + 1):
            b_ball = (N - r * R - g * G)
            b = b_ball // B
            if 0 <= b and b_ball % B == 0:
                ans += 1

    print(ans)

if __name__ == '__main__':
    resolve()
