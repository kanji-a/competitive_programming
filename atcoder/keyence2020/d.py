import itertools
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 可能な並び方を全列挙して、条件にある並び方があったら、
# それになるまでの手数を算出
# 探索 並び順はN!*2^N
print(list(itertools.permutations(range(N))))
# print(list(itertools.permutations(A)))