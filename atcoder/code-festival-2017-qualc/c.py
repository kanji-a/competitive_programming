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
    s = SS()

    s_x = [i for i in s if i != 'x']
    l_s_x = len(s_x)
    for i in range(l_s_x):
        if s_x[i] != s_x[l_s_x-1-i]:
            print(-1)
            return

    x_num = []
    cnt = 0
    for i in s:
        if i == 'x':
            cnt += 1
        else:
            x_num.append(cnt)
            cnt = 0
    if s[-1] == 'x':
        x_num.append(cnt)
    else:
        x_num.append(0)

    len_x_num = len(x_num)
    ans = 0
    for i in range(len_x_num):
        ans += max(x_num[len_x_num-1-i] - x_num[i], 0)

    print(ans)

if __name__ == '__main__':
    resolve()
