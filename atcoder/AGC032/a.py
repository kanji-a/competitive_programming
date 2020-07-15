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
    b = LI()

    # bから数字を除去して空にできるか判定する
    ans = []
    while b:
        has_pop = False
        len_b = len(b)
        for i in range(len_b):
            j = len_b - 1 - i
            if b[j] == j + 1:
                b.pop(j)
                ans.append(j + 1)
                has_pop = True
                break
        if not has_pop:
            break

    if len(ans) == N:
        for i in range(N):
            print(ans[N-1-i])
    else:
        print(-1)

if __name__ == '__main__':
    resolve()
