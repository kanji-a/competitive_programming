import sys, collections
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**10
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

class Node():
    key = None
    p = None
    left = None
    right = None

    def __init__(self, key):
        self.key = key

class BinarySearchTree():
    root = None

    def insert(self, z):
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        
        z.p = y

        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def find(self, k):
        x = self.root
        while x is not None:
            if x.key==k:
                return True
            elif x.key>k:
                x = x.left
            else:
                x = x.right
        return False

    def next_node(self, z):
        if z.right is None:
            if z.p.key>z.key:
                return z.p
            else:
                return None
        else:
            x = z.right
            while x is not None:
                x = x.left
            return x


    def delete(self, z):
        if z.left is None and z.right is None:
            if z.p.key > z.key:
                z.p.left = None
            else:
                z.p.right = None
        elif z.left is not None and z.right is not None:
            y = self.next_node(z)
            z.key = y.key
            self.delete(y)
        else:
            if z.right is None:
                z_child = z.left
            else:
                z_child = z.right
            if z.p.key > z.key:
                z.p.left = z_child
            else:
                z.p.right = z_child
            
    def print_nodes(self):
        inorder = []
        preorder = []

        def dfs(v):
            v_key = v.key
            preorder.append(v_key)
            if v.left is not None:
                dfs(v.left)
            inorder.append(v_key)
            if v.right is not None:
                dfs(v.right)

        dfs(self.root)

        print('', *inorder)
        print('', *preorder)

def resolve():
    m = I()
    T = BinarySearchTree()
    for _ in range(m):
        q = LSS()
        if q[0]=='insert':
            k = int(q[1])
            z = Node(k)
            T.insert(z)
        elif q[0]=='find':
            k = int(q[1])
            if T.find(k):
                print('yes')
            else:
                print('no')
        else:
            T.print_nodes()

if __name__ == '__main__':
    resolve()
