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

    len_S = len(S)
    cnt = collections.Counter(S)

    # 個数が奇数の文字の数
    odd_char_num = [i for i in cnt.values() if i % 2 == 1]

    N = max(len(odd_char_num), 1)

    if odd_char_num:
        # 平均文字数以下の最大奇数
        print((len_S // N - 1) // 2 * 2 + 1)
    else:
        print(len_S)

if __name__ == '__main__':
    resolve()
