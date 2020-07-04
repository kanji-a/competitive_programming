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
    S = SS()

    stk = []
    ans = collections.deque()

    for i in S:
        if i == '(':
            stk.append(i)
        else:
            if stk and stk[-1] == '(':
                stk.pop()
            else:
                ans.appendleft('(')
        ans.append(i)
    
    while stk:
        ans.append(')')
        stk.pop()

    print(''.join(ans))

if __name__ == '__main__':
    resolve()
