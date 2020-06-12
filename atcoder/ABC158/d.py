import sys
input = lambda: sys.stdin.readline().rstrip() 
from collections import deque

def resolve():
    S = input()
    Q = int(input())
    Query = [input().split() for _ in range(Q)]

    S_deque = deque()
    for s in S:
        S_deque.append(s)
 
    is_reversed = False
    for q in Query:
        if q[0]=='1':
            is_reversed = not is_reversed
        elif q[0]=='2':
            if (not is_reversed and q[1]=='1') or (is_reversed and q[1]=='2'):
                S_deque.appendleft(q[2])
            else:
                S_deque.append(q[2])

    if is_reversed:
        S_deque.reverse()

    print(*S_deque, sep='')

if __name__ == '__main__':
    resolve()
