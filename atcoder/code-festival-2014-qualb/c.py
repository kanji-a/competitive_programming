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
    S1 = SS()
    S2 = SS()
    S3 = SS()

    l = len(S1)
    cnt1 = collections.Counter(S1)
    cnt2 = collections.Counter(S2)
    cnt3 = collections.Counter(S3)
    # print(cnt1)
    # print(cnt2)
    # print(cnt3)

    ans = 'YES'
    # 少なくともSxからy文字取ってくる必要があるという情報
    # それが文字列長の半分を越えたらダメ
    at_least_1 = 0
    at_least_2 = 0
    for i in cnt3.keys():
        at_least_1 += max(cnt3[i] - cnt2[i], 0)
        at_least_2 += max(cnt3[i] - cnt1[i], 0)
        if cnt1[i] + cnt2[i] < cnt3[i] or at_least_1 > l // 2 or at_least_2 > l // 2:
            ans = 'NO'
            break

    print(ans)

if __name__ == '__main__':
    resolve()
