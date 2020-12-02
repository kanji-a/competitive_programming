import bisect, collections, copy, heapq, itertools, math, string, sys
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

    has_ans = False
    A = 1
    AA = 3
    while True:
        B = 1
        BB = 5
        while True:
            if AA + BB > N:
                break
            if AA + BB == N:
                has_ans = True
                break
            B += 1
            BB *= 5
        if AA > N or has_ans:
            break
        A += 1
        AA *= 3

    if has_ans:
        print(A, B)
    else:
        print(-1)

if __name__ == '__main__':
    resolve()
