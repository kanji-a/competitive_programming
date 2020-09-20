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
    N, X, M = LI()

    A = []
    seen = set()
    tmp = X
    head_idx = -1
    while True:
        A.append(tmp)
        seen.add(tmp)
        tmp = pow(tmp, 2, M)
        if tmp in seen:
            head_idx = A.index(tmp)
            break
    # print(A, head_idx)

    cnt = [0] * len(A)
    for i in range(len(A)):
        if i < head_idx:
            if i <= N:
                cnt[i] = 1
        else:
            l = len(A) - head_idx
            cnt[i] = (N - head_idx) // l
    for i in range(head_idx, head_idx + (N - head_idx) % l):
        cnt[i] += 1
    # print(cnt)

    ans = sum([a * c for a, c in zip(A, cnt)])
    print(ans)

if __name__ == '__main__':
    resolve()
