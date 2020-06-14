import sys
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

def resolve():

    def maxHeapify(A, i):
        H = len(A)-1
        l = 2*i
        r = 2*i+1
        if l <= H and A[l] > A[i]:
            largest = l
        else:
            largest = i
        if r <= H and A[r] > A[largest]:
            largest = r

        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            maxHeapify(A, largest)

    def maxHeapInsert(A, k):
        S.append(k)
        i = len(S) - 1
        while i!=0:
            maxHeapify(S, i)
            i = i // 2

    def maxHeapPop(A):
        res = A[1]
        A[1] = -1
        i = len(S) - 1
        while i!=0:
            maxHeapify(S, i)
            i = i // 2

        return res

    S = [-1]

    while True:
        order = LSS()
        if order[0] == 'end':
            break
        elif order[0] == 'insert':
            k = int(order[1])
            maxHeapInsert(S, k)
        else:
            ans = maxHeapPop(S)
            print(ans)

if __name__ == '__main__':
    resolve()
