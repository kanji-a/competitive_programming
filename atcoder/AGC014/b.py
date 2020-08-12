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
    N, M = LI()
    cnt = [0] * N
    for _ in range(M):
        a, b = LI_()
        cnt[a] += 1
        cnt[b] += 1

    # 「全ての頂点が偶数回登場する」は必要条件
    # 奇数回登場する頂点があると、それに繋がる辺の中に必ず奇数になる辺が出るから
    # 深さ1の木を考えると、全ての頂点が偶数回登場するならば、
    # 葉iの登場回数=葉iに繋がる辺の数字より、全ての辺の数字が偶数
    if len([i for i in cnt if i % 2 == 0]) == N:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    resolve()
