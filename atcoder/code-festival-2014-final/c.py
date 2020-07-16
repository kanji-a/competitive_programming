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
    A = I()

    def f(N):
        str_N = str(N)
        len_str_N = len(str_N)
        ret = sum([int(e) * N ** (len_str_N - 1 - i) for i, e in enumerate(str_N)])
        return ret

    ans = -1
    for i in range(10, 10001):
        if f(i) == A:
            ans = i

    print(ans)

if __name__ == '__main__':
    resolve()
