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
    s = SS()

    if len(s) == 1:
        print(s + '1')
    else:
        ans = []
        cnt = 1
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                cnt += 1
            else:
                ans.append(s[i])
                ans.append(str(cnt))
                cnt = 1
        ans.append(s[-1])
        if s[-1] == s[-2]:
            ans.append(str(cnt))
        else:
            ans.append('1')

        print(''.join(ans))

if __name__ == '__main__':
    resolve()
