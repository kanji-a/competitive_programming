#!/usr/bin/env python3
import sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**20
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def resolve():
    N, K = LI()
    A = LI_()

    ord = [-1]*N

    city = 0
    cnt = 0
    teleport_path = []
    while ord[city]==-1:
        ord[city] = cnt
        teleport_path.append(city)
        city = A[city]
        cnt += 1
    loop_head = ord[city]
    loop_length = len(teleport_path) - loop_head
    # print(teleport_path, loop_head, loop_length)

    if K-1<loop_head:
        print(teleport_path[K]+1)
    else:
        K = loop_head + (K-loop_head)%loop_length
        print(teleport_path[K]+1)

if __name__ == '__main__':
    resolve()

