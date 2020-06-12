import itertools
import numpy as np

N = int(input())
A = [list(map(int, input().split())) for i in range(N-1)]

def calc_happiness(group):
    happiness = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if(group[i] == group[j]):
                happiness += A[i][j-i-1]
    return happiness

happiness_max = -np.inf
for i in itertools.product(range(3), repeat=N):
    happiness_max = max(calc_happiness(i), happiness_max)

print(happiness_max)