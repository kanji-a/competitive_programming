import sys
input = lambda: sys.stdin.readline().rstrip() 
import math

def resolve():
    R = int(input())

    print(2*math.pi*R)

if __name__ == '__main__':
    resolve()