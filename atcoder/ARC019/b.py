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
    A = SS()

    len_A = len(A)

    cnt = 0
    for i in range(len_A):
        if A[i] != A[len_A-1-i]:
            cnt += 1

    ans = 0
    # すでに回文である場合
    if cnt == 0:
        # 偶数文字の場合、どこを変えても回文ではなくなる
        if len_A % 2 == 0:
            ans = 25 * len_A
        # 奇数文字の場合、真ん中を何に変えても回文にしかならない
        else:
            ans = 25 * (len_A - 1)
    # 変える場所によっては回文になりうる場合
    elif cnt == 2:
        ans = 25 * len_A - 2
    # どこを変えても回文にならない場合
    else:
        ans = 25 * len_A

    print(ans)

if __name__ == '__main__':
    resolve()
