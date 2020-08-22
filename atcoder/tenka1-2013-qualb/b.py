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
    Q, L = LI()

    stk = []
    len_stk = 0

    state = 'SAFE'
    for _ in range(Q):
        query = LSS()
        if query[0] == 'Push':
            N = int(query[1])
            M = int(query[2])
            if len_stk > L - N:
                state = 'FULL'
                break
            len_stk += N
            stk.append((N, M))
        elif query[0] == 'Pop':
            N = int(query[1])
            if len_stk < N:
                state = 'EMPTY'
                break
            len_stk -= N
            while stk and N >= stk[-1][0]:
                n, _ = stk.pop()
                N -= n
            if stk:
                n, m = stk.pop()
                stk.append((n - N, m))
        elif query[0] == 'Top':
            if not stk:
                state = 'EMPTY'
                break
            print(stk[-1][1])
        elif query[0] == 'Size':
            print(len_stk)
        # print(stk, len_stk)
    print(state)

if __name__ == '__main__':
    resolve()
