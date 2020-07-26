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

    suit_list = ('S', 'H', 'D', 'C')
    rsf_num_list = ('10', 'J', 'Q', 'K', 'A')
    rsf_suit_id = {}
    rsf_num_id = {}
    for i in range(4):
        rsf_suit_id[suit_list[i]] = i
    for i in range(5):
        rsf_num_id[rsf_num_list[i]] = i

    # 最も早くロイヤルストレートフラッシュができるスートを求める
    turned = []
    rsf = [[False] * 5 for _ in range(4)]
    i = 0
    while i < len(s):
        suit = s[i]
        i += 1
        if s[i] == '1':
            num = '10'
            i += 2
        else:
            num = s[i]
            i += 1

        if num in rsf_num_list:
            rsf[rsf_suit_id[suit]][rsf_num_id[num]] = True
        if 5 in [i.count(True) for i in rsf]:
            suit_num = [i.count(True) for i in rsf].index(5)
            break

        turned.append((suit, num))

    # ロイヤルストレートフラッシュに使った札を除外して山札列挙
    ans = [i for i in turned if i[0] != suit_list[suit_num] or i[1] not in rsf_num_list]
    if len(ans) == 0:
        print(0)
    else:
        print(''.join([i + j for i, j in ans]))

if __name__ == '__main__':
    resolve()
