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

    if N % 2 == 0:
        print(N, N, N // 2)
    else:
        ans = (0, 0, 0)
        for h in range(1, 3501):
            # hが1だとPythonでTLE
            for n in range(h, 3501):
                # 式をwについて解いた
                num = N * n * h
                denom = 4 * h * n - N * (h + n)
                if denom > 0 and num % denom == 0:
                    w = num // denom
                    ans = (h, n, w)
                    break

        print(*ans)

if __name__ == '__main__':
    resolve()
