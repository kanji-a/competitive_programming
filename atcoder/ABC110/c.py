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
    R0 = [-1] * 26
    R1 = [-1] * 26

    is_ok = True
    for i in range(l):
        S_num = ord(S[i]) - ord('a')
        T_num = ord(T[i]) - ord('a')
        # print(S_num, T_num)
        if R0[S_num] == -1:
            R0[S_num] = T_num
        else:
            if R0[S_num] != T_num:
                is_ok = False 
                break
        if R1[T_num] == -1:
            R1[T_num] = S_num
        else:
            if R1[T_num] != S_num:
                is_ok = False 
                break

    if is_ok:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    resolve()
