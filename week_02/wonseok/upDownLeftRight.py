N = int(input())
M = list(map(str, input().split()))

# (L, R, U, D)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def movement(result, direction):
    new_x = result[0] + dx[direction]
    new_y = result[1] + dy[direction]
    if new_x==0 or new_x==6 or new_y==0 or new_y==6:
      result = result
    else:
      result[0] = new_x
      result[1] = new_y
    return result
      
result = [1, 1]
for move in M:
  if move == "L":
    result = movement(result, 0)
  elif move == "R":
    result = movement(result, 1)
  elif move == "U":
    result = movement(result, 2)
  elif move == "D":
    result = movement(result, 3)

print(result)
