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
    H, W = LI()
    a = []
    for _ in range(H):
        a.append(SS())
    a = ''.join(a)

    # not 中央行 and not 中央列 の文字は4n個
    # 中央行 xor 中央列 は2n or 4n個
    # 中央行中央列 は1個
    cnt = collections.Counter(a)
    l = list(cnt.values())
    c4 = len([i for i in l if i % 4 == 0])
    c2 = len([i for i in l if i % 4 == 2])
    c1 = len([i for i in l if i % 4 == 1])
    # print(cnt)
    # print(c4, c2, c1)

    if H % 2 == W % 2 == 0:
        if c4 == len(cnt):
            print('Yes')
        else:
            print('No')
    elif H % 2 == W % 2 == 1:
        if c1 == 1 and c2 <= (H + W - 2) // 2 and c4 + c2 + c1 == len(cnt):
            print('Yes')
        else:
            print('No')
    else:
        if H % 2 == 1:
            if c2 <= W // 2 and c4 + c2 == len(cnt):
                print('Yes')
            else:
                print('No')
        if W % 2 == 1:
            if c2 <= H // 2 and c4 + c2 == len(cnt):
                print('Yes')
            else:
                print('No')
            
if __name__ == '__main__':
    resolve()
