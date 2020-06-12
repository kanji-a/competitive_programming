import numpy as np

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

print(H, W)
print(A)

stack = [(H-1, 0)]
cost_min = -np.inf
visited = [[False for _ in range(W)] for _ in range(H)]

cost = 0
while len(stack) > 0:
    current = stack.pop()
    print("current: ", current)
    cost += A[current[0]][current[1]]
    visited[current[0]][current[1]] = True
    if current == (H-1, W-1):
        print("goal")
    neighbor_down = (current[0]+1, current[1])
    if neighbor_down[0] <= H-1 and not visited[neighbor_down[0]][neighbor_down[1]]:
        stack.append(neighbor_down)
    neighbor_up = (current[0]-1, current[1])
    if neighbor_up[0] >= 0 and not visited[neighbor_up[0]][neighbor_up[1]]:
        stack.append(neighbor_up)
    neighbor_right = (current[0], current[1]+1)
    if neighbor_right[1] <= W-1 and not visited[neighbor_right[0]][neighbor_right[1]]:
        stack.append(neighbor_right)
    neighbor_left = (current[0], current[1]-1)
    if neighbor_left[1] >= 0 and not visited[neighbor_left[0]][neighbor_left[1]]:
        stack.append(neighbor_left)