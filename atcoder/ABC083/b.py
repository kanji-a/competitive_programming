N, A, B = map(int, input().split())

def digitSum(x):
    return sum(map(int, list(str(x))))

print(sum(filter(lambda x: A <= digitSum(x) <= B, range(1, N+1))))