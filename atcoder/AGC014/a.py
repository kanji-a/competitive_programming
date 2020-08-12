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
    A, B, C = LI()

    s = set()
    ans = 0
    while A % 2 == B % 2 == C % 2 == 0:
        s.add((A, B, C))
        tmp_A = A
        tmp_B = B
        tmp_C = C
        A = tmp_B // 2 + tmp_C // 2
        B = tmp_C // 2 + tmp_A // 2
        C = tmp_A // 2 + tmp_B // 2
        if (A, B, C) in s:
            ans = -1
            break
        ans += 1

    print(ans)

if __name__ == '__main__':
    resolve()
