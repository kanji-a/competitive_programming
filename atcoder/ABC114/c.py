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

    ans = [0]

    def dfs(num):
        if not num or num and int(''.join(num)) <= N:
            if num.count('7') >= 1 and num.count('5') >= 1 and num.count('3') >= 1:
                ans[0] += 1
            for i in ('7', '5', '3'):
                num.append(i)
                dfs(num)
                num.pop()

    dfs([])
    
    print(ans[0])

if __name__ == '__main__':
    resolve()
