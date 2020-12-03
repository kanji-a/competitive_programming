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
    A = LI()

    # 残った値のMaxはsum(B) - sum(C)
    # BもCもAの部分列でサイズ1以上
    # BとCはAを2つに分割したもの
    B = []
    C = []
    A_p = []
    A_n = []
    A_z = []
    for i in A:
        if i == 0:
            A_z.append(i)
        elif i > 0:
            A_p.append(i)
        else:
            A_n.append(i)
    A_p.sort()
    A_n.sort(reverse=True)

    if A_p:
        if A_n:
            B = A_p + A_z
            C = A_n
        else:
            if A_z:
                B = A_p
                C = A_z
            else:
                B = A_p[1:]
                C = A_p[:1]
    else:
        if A_n:
            if A_z:
                B = A_z
                C = A_n
            else:
                B = A_n[:1]
                C = A_n[1:]
        else:
            B = A_z[:1]
            C = A_z[1:]

    M = sum(B) - sum(C)
    print(M)
    if len(B) == 1:
        # B[0]からCを引くだけ
        num = B[0]
        for i in C:
            print(num, i)
            num -= i
    else:
        # Bを足すために、一旦C[0]からB[1:]を全部引いて、それをB[0]から引く
        # その後はC[1:]を引くだけ
        num = C[0]
        for i in B[1:]:
            print(num, i)
            num -= i
        print(B[0], num)
        num = B[0] - num
        for i in C[1:]:
            print(num, i)
            num -= i

if __name__ == '__main__':
    resolve()
