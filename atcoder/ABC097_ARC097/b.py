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
    X = I()

    ans = 0
    for i in range(1, int(X ** 0.5) + 1):
        for j in range(2, max(int(math.log2(X)) + 1, 3)):
            tmp = i ** j
            if tmp <= X:
                ans = max(tmp, ans)

    print(ans)

if __name__ == '__main__':
    resolve()
