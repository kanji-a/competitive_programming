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

    cnt = collections.Counter(A)
    # 同じ数字3枚引いて1, 2枚になるまで減らす
    for i in cnt.keys():
        if cnt[i] % 2 == 0:
            cnt[i] = 2
        else:
            cnt[i] = 1

    ans = 0
    even_num = [i for i in cnt.keys() if cnt[i] == 2]
    # 2枚ある2種類の数字から3枚引けば1枚ずつにできる
    if len(even_num) % 2 == 0:
        ans = len(cnt)
    else:
        # 2枚ある数字が1種類残ったらそれらと別の数字を引く
        ans = len(cnt) - 1

    print(ans)

if __name__ == '__main__':
    resolve()
