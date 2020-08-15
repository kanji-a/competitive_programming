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

    idx = [0]

    def dfs():
        if S[idx[0]] != '{':
            while '0' <= S[idx[0]] <= '9':
                idx[0] += 1
            return 'INTEGER'
        
        idx[0] += 1
        if S[idx[0]] == '}':
            idx[0] += 1
            return 'DICT'

        dfs()
        if S[idx[0]] == ':':
            idx[0] += 1
            dfs()
            while S[idx[0]] != '}':
                idx[0] += 1
                dfs()
            return 'INTEGER'



if __name__ == '__main__':
    resolve()
