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
    s = list(SS())
    K = I()

    # 左からaにしていって、余ったKを一番右に突っ込む
    for i in range(len(s) - 1):
        diff = (ord('a') - ord(s[i])) % 26
        if K >= diff:
            K -= diff
            s[i] = 'a'

    if K > 0:
        s[-1] = chr((ord(s[-1]) - ord('a') + K) % 26 + ord('a'))
    
    print(''.join(s))

if __name__ == '__main__':
    resolve()
