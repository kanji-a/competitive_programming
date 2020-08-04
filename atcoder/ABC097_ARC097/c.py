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
    K = I()

    l = [[] for _ in range(26)]
    for i in range(len(s)):
        l[ord(s[i])-ord('a')].append(i)

    for i in l:
        tmp = set()
        for j in i:
            for k in range(5):
                if j + k <= len(s) - 1:
                    tmp.add(s[j:j+k+1])
        tmp = list(tmp)
        tmp.sort()
        if len(tmp) >= K:
            print(tmp[K-1])
            break
        else:
            K -= len(tmp)

if __name__ == '__main__':
    resolve()
