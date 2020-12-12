import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 10**9+7
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    c = SS()
    len_c = len(c)

    if c == 'a' or c == 'z' * 20:
        print('NO')
    else:
        if len(set(c)) == 1:
            # 全部同じ文字の場合
            if c[0] == 'a':
                # 全部aであれば、最初をbにして最後を消す
                print('b' + 'a' * (len_c - 2))
            elif len_c == 20:
                # 長さ20であれば、最初を1戻して次を1進める
                print(chr(ord(c[0]) - 1) + chr(ord(c[1]) + 1) + c[2:])
            else:
                # 全部aでなく長さ19以下であれば、最初を1戻して最後にaを足す
                print(chr(ord(c[0]) - 1) + c[1:] + 'a')
        else:
            # サイクリックシフト
            print(c[1:] + c[0])
        
if __name__ == '__main__':
    resolve()
