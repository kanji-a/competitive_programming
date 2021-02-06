#!/usr/bin/env python3
import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)
INF = float('inf')
MOD = 10 ** 9 + 7
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N, K = LI()
    S = [SS() for _ in range(N)]

    cnt = collections.Counter(S)
    # K番目の単語は出現回数がいくつか、その出現回数の単語は何種類あるか
    words = [(v, k) for k, v in cnt.items()]
    words.sort(reverse=True)
    num = words[K-1][0]
    ans = [i for i in cnt.keys() if cnt[i] == num]
    if len(ans) == 1:
        print(ans[0])
    else:
        print('AMBIGUOUS')

if __name__ == '__main__':
    resolve()

