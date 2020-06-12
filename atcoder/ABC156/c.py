import sys
input = lambda: sys.stdin.readline().rstrip() 
import numpy as np

def resolve():
    N = int(input())
    X = list(map(int, input().split()))

    minpower = np.inf
    for P in range(1, max(X)+1):
        minpower = min(sum([(x-P)**2 for x in X]), minpower)

    print(minpower)

if __name__ == '__main__':
    resolve()
