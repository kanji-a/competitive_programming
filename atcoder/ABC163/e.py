import sys
input = lambda: sys.stdin.readline().rstrip() 
import itertools

def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    dist = set()
    for i in itertools.permutations(range(4)):
        tmp = sorted([str(i[0]-0), str(abs(i[1]-1)), str(abs(i[2]-2)), str(abs(i[3]-3))])
        # tmp = sorted([i[0]-0, abs(i[1]-1), abs(i[2]-2), abs(i[3]-3)])
        dist.add(''.join(tmp))

    print(dist)

if __name__ == '__main__':
    resolve()
