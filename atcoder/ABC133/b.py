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
    N, D = LI()
    X = [LI() for _ in range(N)]

    MAX_DIST = 16000
    square_num = set()
    i = 1
    while i ** 2 <= MAX_DIST:
        square_num.add(i ** 2)
        i += 1

    ans = 0
    for i, j in itertools.combinations(range(N), 2):
        if sum([(k - l) ** 2 for k, l in zip(X[i], X[j])]) in square_num:
            ans += 1

    print(ans)

if __name__ == '__main__':
    resolve()
