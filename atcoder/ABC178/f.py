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
    B = LI()

    cnt_A = collections.Counter(A)
    cnt_B = collections.Counter(B)

    # Noになる条件:十分条件AとBで個数の合計がNより大きい数字が存在する場合
    exists = True
    # offset = 0
    most_freq_common_num = 0
    freq = 0
    for i in set(cnt_A.keys()) & set(cnt_B.keys()):
        # offset = max(cnt_A[i], cnt_B[i], offset)
        if max(cnt_A[i], cnt_B[i]) > freq:
            most_freq_common_num = i
            freq = max(cnt_A[i], cnt_B[i])
        if cnt_A[i] + cnt_B[i] > N:
            exists = False
            break

    if exists:
        print('Yes')
        # print(A.index(most_freq_common_num), cnt_A[most_freq_common_num])
        # print(B.index(most_freq_common_num), cnt_B[most_freq_common_num])
        offset = 0
        if most_freq_common_num != 0:
            offset = (A.index(most_freq_common_num) + cnt_A[most_freq_common_num]) - B.index(most_freq_common_num)
        # print(offset)
        print(*(B * 2)[offset:offset+N])
    else:
        print('No')

if __name__ == '__main__':
    resolve()
