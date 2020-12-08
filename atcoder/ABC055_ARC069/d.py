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
    N = I()
    s = SS()

    d = {0: 'S', 1: 'W'}
    has_ans = False
    # 0, 1番目を決めると、全てが順番に決まる
    for i, j in itertools.product(range(2), repeat=2):
        ans = [i, j]
        for k in range(1, N - 1):
            if ans[k] == 0 and s[k] == 'o' or ans[k] == 1 and s[k] == 'x':
                ans.append(ans[k-1])
            else:
                ans.append(1 - ans[k-1])
        # 最初に決めた0, 1番目と、1週して決め直した0, 1番目に矛盾がなければ答え
        ans_second = []
        for k in range(-1, 1):
            if ans[k] == 0 and s[k] == 'o' or ans[k] == 1 and s[k] == 'x':
                ans_second.append(ans[k-1])
            else:
                ans_second.append(1 - ans[k-1])
        # print(ans, ans_second)
        if ans_second == ans[:2]:
            has_ans = True
            break

    if has_ans:
        print(''.join([d[k]for k in ans]))
    else:
        print(-1)

if __name__ == '__main__':
    resolve()
