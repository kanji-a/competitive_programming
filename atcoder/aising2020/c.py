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

    xyz_max = int(N ** 0.5) + 1
    ans = [0] * (N + 1)
 
    for x, y, z in itertools.product(range(1, xyz_max), range(1, xyz_max), range(1, xyz_max)):
        n = x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x
        if n <= N:
            ans[n] += 1

    for i in range(1, N + 1):
        print(ans[i])

if __name__ == '__main__':
    resolve()
