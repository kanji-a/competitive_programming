import sys
input = sys.stdin.readline

N = int(input())
p = list(map(int, [input() for _ in range(N)]))
Q = int(input())
ab = [list(map(int, input().split())) for _ in range(Q)]

# print(N)
# print(p)
# print(Q)
# print(ab)

def isChild(a, b):
    a = a
    while p[a-1] != -1:
        if p[a-1] == b:
            return True
        else:
            a = p[a-1]

if __name__ == '__isChild__':
    isChild()

for i in range(Q):
    if isChild(ab[i][0], ab[i][1]):
        print('Yes')
    else:
        print('No')
        