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

    # A.sort(reverse=True)
    cnt = collections.Counter(A)
    keys = list(cnt.keys())
    keys.sort(reverse=True)
    values = [cnt[i] for i in keys]
    values_acc = [0] * (len(values) + 1)
    for i in range(len(values)):
        values_acc[i+1] = values_acc[i] + values[i]

    ans = 0
    for i in range(len(values)):
        if values[i] <= values_acc[i]:
            ans += keys[i] * values[i]
        else:
            ans += keys[i] * values[i]



    print(keys)
    print(values)
    print(values_acc)

if __name__ == '__main__':
    resolve()
