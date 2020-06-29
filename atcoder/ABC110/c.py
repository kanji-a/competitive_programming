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
    S = SS()
    T = SS()

    l = len(S)

    S_i = [[] for _ in range(26)]
    T_i = [[] for _ in range(26)]
    for i in range(l):
        S_i[ord(S[i]) - ord('a')].append(i)
        T_i[ord(T[i]) - ord('a')].append(i)

    S_set = set()
    T_set = set()
    for i in range(26):
        if S_i[i]: S_set.add(tuple(S_i[i]))
        if T_i[i]: T_set.add(tuple(T_i[i]))

    if S_set == T_set:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    resolve()
