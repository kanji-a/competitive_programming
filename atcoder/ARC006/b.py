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
    N, L = LI()
    amida_raw = [SS() for _ in range(L)]
    result_raw = SS()

    amida = []
    for i in amida_raw:
        tmp = []
        for j in range(N - 1):
            if i[j*2+1] == '-':
                tmp.append(j)
        amida.append(tmp)

    result = (len(result_raw) - 1) // 2

    cur = result
    for i in reversed(amida):
        if cur in i:
            cur += 1
        elif cur - 1 in i:
            cur -= 1

    print(cur + 1)

if __name__ == '__main__':
    resolve()
