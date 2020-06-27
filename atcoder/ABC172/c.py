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
    N, M, K = LI()
    A = collections.deque(LI())
    B = collections.deque(LI())

    ans = 0
    while K > 0:
        if A and not B or (A and B and A[0] < B[0]):
            if K < A[0]:
                break
            K -= A[0]
            A.popleft()
            ans += 1
        elif B and not A or A and B and A[0] > B[0]:
            if K < B[0]:
                break
            K -= B[0]
            B.popleft()
            ans += 1
        else:
            break

    print(ans)


if __name__ == '__main__':
    resolve()
