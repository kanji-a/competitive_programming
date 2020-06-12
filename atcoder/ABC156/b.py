import sys
input = lambda: sys.stdin.readline().rstrip() 
import math
 
def resolve():
    N, K = map(int, input().split())
    print(math.floor(math.log(N, K))+1)
 
if __name__ == '__main__':
    resolve()