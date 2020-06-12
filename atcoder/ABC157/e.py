import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():

    class BinaryIndexedTree:
        def __init__(self, n):
            self.size = n
            self.tree = [0] * (n + 1)
    
        def sum(self, i):
            s = 0
            while i > 0:
                s += self.tree[i]
                i -= i & -i
            return s
    
        def add(self, i, x):
            while i <= self.size:
                self.tree[i] += x
                i += i & -i

    N = int(input())
    S = list(input())
    Q = int(input())
    Query = [input().split() for _ in range(Q)] 

    pos_bit_list = [BinaryIndexedTree(len(S)) for _ in range(26)]

    for i, c in enumerate(S):
        pos_bit_list[ord(c)-ord('a')].add(i+1, 1)

    for q in Query:
        if q[0] == '1':
            i = int(q[1])
            c = q[2]
            pos_bit_list[ord(S[i-1])-ord('a')].add(i, -1)
            pos_bit_list[ord(c)-ord('a')].add(i, 1)
            S[i-1] = c
        else:
            print(len([p for p in pos_bit_list if p.sum(int(q[2])) - p.sum(int(q[1])-1) > 0]))

if __name__ == '__main__':
    resolve()
